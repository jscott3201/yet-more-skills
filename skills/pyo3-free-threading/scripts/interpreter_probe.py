#!/usr/bin/env python3
"""Inspect explicit trusted imports in a bounded Python child; never change GIL mode.

Python 3.11+. Only the selected child interpreter/environment is inspected.
The result observes imports and GIL state, not general thread safety.
"""
from __future__ import annotations

import argparse
import importlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import sysconfig
import tempfile
from typing import Any


def gil_enabled() -> bool | None:
    """Unknown is distinct from disabled, including interpreters without this API."""
    inspect = getattr(sys, "_is_gil_enabled", None)
    if not callable(inspect):
        return None
    try:
        value = inspect()
    except Exception:
        return None
    return value if isinstance(value, bool) else None


def observe(modules: list[str]) -> dict[str, Any]:
    """Run in the selected interpreter. Imports execute trusted module code."""
    raw_build = sysconfig.get_config_var("Py_GIL_DISABLED")
    free_build = None if raw_build is None else raw_build in (1, "1")
    result: dict[str, Any] = {
        "executable": sys.executable,
        "version": sys.version,
        "implementation": sys.implementation.name,
        "platform": sys.platform,
        "machine": __import__("platform").machine(),
        "free_threaded_build": free_build,
        "gil_before_imports": gil_enabled(),
        "gil_mode_overrides": {
            "PYTHON_GIL": os.environ.get("PYTHON_GIL"),
            "xoption_gil": sys._xoptions.get("gil"),
        },
        "isolated": bool(sys.flags.isolated),
        "imports": [],
    }
    for name in modules:
        step: dict[str, Any] = {"module": name, "gil_before": gil_enabled()}
        try:
            module = importlib.import_module(name)
            step.update(ok=True, origin=getattr(module, "__file__", None))
        except Exception as error:
            step.update(ok=False, error_type=type(error).__name__, error=str(error))
        step["gil_after"] = gil_enabled()
        result["imports"].append(step)
    result["gil_after_imports"] = gil_enabled()
    return result


def assess(report: dict[str, Any], require_disabled: bool) -> tuple[int, str]:
    """Classify observations without treating absent evidence as a pass."""
    if any(not entry["ok"] for entry in report["imports"]):
        return 1, "import_failed"
    states = [report["gil_before_imports"], report["gil_after_imports"]]
    for entry in report["imports"]:
        states.extend((entry["gil_before"], entry["gil_after"]))
    disabled = report["free_threaded_build"] is True and all(x is False for x in states)
    if require_disabled and not disabled:
        return 2, "disabled_gil_not_verified"
    return 0, "observed_disabled_gil" if disabled else "observed_only"


def module_name(value: str) -> str:
    if not value or not all(part.isidentifier() for part in value.split(".")):
        raise argparse.ArgumentTypeError("Use a dotted import module name, not a path or code.")
    return value


def positive_timeout(value: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("Timeout must be finite and greater than zero.")
    return number


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--python", default=sys.executable, help="Target interpreter executable.")
    parser.add_argument("--module", action="append", type=module_name, default=[],
                        help="Trusted module to import, in order; repeat for dependencies.")
    parser.add_argument("--timeout", type=positive_timeout, default=30.0,
                        help="Maximum child runtime in seconds (default: 30).")
    parser.add_argument("--isolated", action="store_true", help="Start target Python with -I.")
    parser.add_argument("--require-gil-disabled", action="store_true",
                        help="Exit 2 unless build and all observed runtime states prove disabled GIL.")
    parser.add_argument("--_child-output", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args._child_output is not None:
        args._child_output.write_text(json.dumps(observe(args.module)), encoding="utf-8")
        return 0
    if not args.module:
        parser.error("At least one explicit --module is required.")
    with tempfile.TemporaryDirectory(prefix="python-binding-probe-") as tmp:
        output = Path(tmp) / "observation.json"
        command = [args.python]
        if args.isolated:
            command.append("-I")
        command += [str(Path(__file__).resolve()), "--_child-output", str(output)]
        for name in args.module:
            command += ["--module", name]
        try:
            child = subprocess.run(command, capture_output=True, text=True,
                                   encoding="utf-8", errors="replace", timeout=args.timeout)
            if child.returncode != 0 or not output.is_file():
                report = {"status": "probe_error", "child_exit": child.returncode,
                          "error": "Target interpreter did not complete the observation."}
                code = 1
            else:
                report = json.loads(output.read_text(encoding="utf-8"))
                code, report["status"] = assess(report, args.require_gil_disabled)
            # Import output cannot corrupt the structured result. Keep diagnostics bounded.
            if child.stdout:
                report["child_stdout_excerpt"] = child.stdout[-2000:]
            if child.stderr:
                report["child_stderr_excerpt"] = child.stderr[-2000:]
        except subprocess.TimeoutExpired:
            report, code = {"status": "probe_error", "error": "Target interpreter timed out."}, 1
        except (OSError, ValueError, KeyError, TypeError) as error:
            report, code = {"status": "probe_error", "error": str(error)}, 1
    print(json.dumps(report, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())

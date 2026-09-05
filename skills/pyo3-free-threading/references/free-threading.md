# Validation details

The probe requires Python 3.11+ for this package's tooling. Invoke it using an available ordinary interpreter as the supervisor; `--python` names the interpreter whose environment will be inspected. No dependency installation or compilation occurs. Imports execute module code: only inspect modules you intend to trust and test. Do not run it against production processes or pass secrets as module arguments.

Example from this skill's directory, replacing the interpreter and module with the real installed targets:

```bash
python3 scripts/interpreter_probe.py --python /path/to/python3.14t   --module rusty_modbus --isolated --require-gil-disabled
```

Repeat `--module` for dependencies whose import effects should be visible in order. The JSON contains build/runtime observations, imported paths, errors, and GIL state per step. Nonzero status distinguishes runtime inspection failure from unmet disabled-GIL requirement. A successful strict probe means only that the sampled imports succeeded and the observed states stayed disabled on a free-threaded build.

Run normal startup without externally forcing the GIL off before claiming modules advertise compatibility. Then, where safe and authorized, run concurrency tests in the desired mode. Testing ordinary CPython alone cannot exercise missing-GIL races. Testing two disjoint objects cannot establish safety for shared-object mutation. No finite stress test proves absence of all races, so preserve the ownership argument too.

The PyO3 0.29.2 free-threading chapter still contains an older blanket limited-API caveat. Its feature/distribution reference, Maturin, and CPython 3.15 documentation describe abi3t. Use those ABI-specific sources for packaging; retain the free-threading chapter for attachment and synchronization mechanics. For Python 3.14t, version-specific native wheels remain a distinct case.

Primary references: [CPython free-threading HOWTO](https://docs.python.org/3.14/howto/free-threading-python.html), [PyO3 free-threading](https://pyo3.rs/v0.29.2/free-threading), [PyO3 ABI features](https://pyo3.rs/v0.29.2/features), [synchronization APIs](https://pyo3.rs/main/doc/pyo3/sync/index.html), [pyclass thread safety](https://pyo3.rs/v0.29.2/class/thread-safety).

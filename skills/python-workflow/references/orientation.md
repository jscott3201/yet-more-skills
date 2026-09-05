# Orientation and routing

A nested pyproject.toml can describe a separate project from the repository root. Find the working directory expected by existing scripts before using a package manager. A development install is useful for iteration; it is not release evidence. The Python runner, build interpreter, and final consumer must be the intended executables, not simply identically named `python` commands.

Start with `python -VV`, `python -c "import sys; print(sys.executable)"`, and the project's own documented test command. These examples use the selected interpreter; substitute its full path when needed. Inspect configured tools before executing them. `uv run` can synchronize environments and update locks; use its documented locked mode when preserving an established uv project. Do not create a uv project just to run an existing pip/maturin workflow.

A suitable change summary names the public behavior, a regression, tested environments, and what was not run. Small Python edits need no architecture ceremony. New dependencies and a new runtime baseline are product decisions, not incidental cleanup.

Inspect package metadata and exported APIs in the actual repository; do not infer its support matrix from an unrelated example.

Primary references: [uv project workflow](https://docs.astral.sh/uv/guides/projects/), [pytest integration](https://docs.pytest.org/en/stable/explanation/goodpractices.html), [Codex skills](https://developers.openai.com/codex/skills).

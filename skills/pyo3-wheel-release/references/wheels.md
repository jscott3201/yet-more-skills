# ABI and wheel checks

As of 2026-09-05, PyO3 0.29.2 documents abi3 for ordinary CPython and abi3t for CPython 3.15+ across ordinary/free-threaded variants. Maturin documents corresponding wheel tags, including an abi3.abi3t combined tag where applicable; Python 3.14t uses a version-specific cp314-cp314t case. Treat these as current capabilities, not a mandate to turn them on in an older pinned project. Python 3.15 is still prerelease at this research date.

There is a documentation inconsistency: the PyO3 free-threading chapter retains a blanket statement that no limited-API equivalent exists. The ABI feature/distribution pages and CPython 3.15 abi3t migration guide are more specific and current for that question. Follow those, verify installed tool support, and test artifact tags. Do not generalize the old 3.14t restriction to every future interpreter.

A practical build shape, from the real binding package, is `maturin build --release --interpreter /path/to/python`. Confirm flags against the installed version and keep project features/configuration rather than overwriting them. For sdist reconstruction, use the declared PEP 517 backend in a clean source extraction with explicitly selected tooling. Do not build a native release using a random Python found first on PATH.

Installation checks should include distribution version versus module version, import origin, public submodules, exception classes, call signatures/defaults, awaitable semantics, and type-checker consumer examples. Test stubs on the oldest supported syntax level. Native signature introspection can be incomplete, so generated stub comparisons are supplementary to calling the real API.

Primary references: [PyO3 ABI features](https://pyo3.rs/v0.29.2/features), [building/distribution](https://pyo3.rs/v0.29.2/building-and-distribution), [Maturin bindings](https://www.maturin.rs/bindings.html), [Maturin distribution](https://www.maturin.rs/distribution.html), [CPython abi3t migration](https://docs.python.org/3.15/howto/abi3t-migration.html), [typing distribution](https://typing.python.org/en/latest/spec/distributing.html), [Python 3.15 schedule](https://peps.python.org/pep-0790/).

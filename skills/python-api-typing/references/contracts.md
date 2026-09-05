# Contract checks

For a register-read SDK, clarify whether results are snapshots, mutable lists, or views over native storage. An `int` annotation alone cannot express the 16-bit wire range. For a graph API, clarify whether a handle owns the graph, references a session, or becomes invalid on close. For Haystack, Marker, NA, Remove, and Null are different concepts; do not represent all of them as Optional values merely for typing convenience.

A public extension wrapper can expose dynamic submodules at runtime. Check both `import package.submodule` and `from package.submodule import Symbol`, and ensure the installed stubs describe the same structure. Inspect whether module initialization registers dynamic submodules in `sys.modules`.

A stub-validation tool such as mypy.stubtest can detect some inconsistencies, but do not add it as a second type checker by default. Native introspection limitations need focused, explained exclusions and behavioral calls, not a blanket allowlist. For an inline-typed package, place py.typed appropriately; for a stub-only or extension-module layout, use the packaging rules for that layout. A marker file in an arbitrary wheel location proves nothing about checker discovery.

Use the repository's chosen checker with its supported CLI. Verify exports from an isolated consumer rather than a path that resolves local source or hand-added stub directories.

Primary references: [typing distribution specification](https://typing.python.org/en/latest/spec/distributing.html), [typing protocols](https://typing.python.org/en/latest/spec/protocol.html), [mypy stubtest](https://mypy.readthedocs.io/en/stable/stubtest.html), [PyO3 signatures](https://pyo3.rs/v0.29.2/function/signature).

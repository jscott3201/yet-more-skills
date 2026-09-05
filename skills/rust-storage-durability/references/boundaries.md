# Storage ownership boundaries

Keep persistence mechanics below query and graph semantics. Planned storage formats and execution features are not evidence of implemented behavior.

Protect authoritative manifest selection and the lifetime of referenced snapshot/WAL files with the repository's documented ownership mechanism. A returned checkpoint path does not itself grant retention ownership. Preserve recovery lock order and callback non-reentrancy.

Treat primary values as authoritative and derived indexes as rebuildable. Verify index visibility and candidate invalidation on update, delete, and recovery, not only recall on a newly built index.

Recursive value validation must agree across schema representation, materialization, inspection, replay, and snapshots. Validating only an outer container can violate the stored value contract.

Reference: [Rust file synchronization](https://doc.rust-lang.org/std/fs/struct.File.html). Inspect current source and tests before applying these checks.

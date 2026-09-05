# Deepening a module

Deepening consolidates caller coordination behind a smaller, more useful interface. It is justified when evidence shows repeated policy, scattered invariants, duplicated recovery, or tests that must understand several internal modules to express one behavior.

## Classify dependencies

- **In-process:** pure computation or memory. Test directly through the proposed interface.
- **Local substitute:** filesystem, database, queue, or service with a faithful local implementation. Prefer the supported substitute when its contract is adequate.
- **Owned remote:** another owned process or service. Keep transport in an adapter and preserve the owned cross-service contract.
- **External:** a third-party service. Isolate vendor behavior behind the smallest owned contract that the application actually needs.

These categories guide testing; they do not prescribe a pattern. Verify latency, failure, transaction, consistency, and lifecycle constraints before moving a seam.

## Safe change shape

1. Record behavior and callers at the existing interface.
2. Define the proposed interface and compatibility path.
3. Add tests that protect observable behavior at the new or retained seam.
4. Migrate callers in bounded, green steps.
5. Remove old paths only after coverage and callers prove them unused.

Retain useful lower-level tests when they protect a distinct contract or diagnose failures cheaply. Consolidation is not evidence that every prior test is waste.

# Expand, migrate, contract

Use this sequence when a shared contract, schema, or symbol cannot be changed atomically while keeping callers green.

1. **Expand:** introduce the new form beside the old one, including compatibility behavior and evidence that existing callers still work.
2. **Migrate:** move bounded caller groups to the new form. Size groups by ownership and blast radius, not arbitrary file counts. Each migration slice should be independently verifiable.
3. **Contract:** remove the old form only after search, graph coverage, runtime evidence where applicable, and all migration blockers prove no supported caller remains.

Declare the compatibility window, source owner, generated artifacts, rollout/recovery behavior, and the evidence that permits contraction. A schema migration, lockfile, generator, public contract, or shared authority surface may require a serial foundation slice before caller work begins.

If no intermediate state can stay valid, do not disguise the change as independent tickets. Replan around an integration branch, coordinated release, feature flag, or other owner-approved migration boundary.

# Comparing interface alternatives

Use this when the interface itself is a material decision.

Frame the same constraints for every candidate: callers, required behaviors, invariants, errors, performance, compatibility, dependencies, and migration limits. Produce at least two structurally different designs rather than cosmetic variations.

For each candidate, show:

1. interface shape and a representative call;
2. invariants, ordering, errors, and configuration a caller must know;
3. behavior hidden behind the interface;
4. dependency and adapter strategy;
5. test seam and failure injection;
6. migration and compatibility cost;
7. leverage, locality, and known weak spots.

Use independent read-only design lanes only when delegation is authorized and would produce real diversity. Otherwise develop the alternatives directly. Recommend one candidate or a clearly defined hybrid, and identify any choice that must be made by the owner.

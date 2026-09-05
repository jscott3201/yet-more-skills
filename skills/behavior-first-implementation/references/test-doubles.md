# Test doubles at boundaries

Prefer real in-process collaborators and repository-supported local substitutes. Introduce a double when it isolates a true external boundary, makes nondeterminism controllable, or is the established test contract.

Useful boundary doubles include:

- third-party APIs and message transports;
- time, randomness, and schedulers;
- slow or unavailable remote services;
- failure injection that cannot be triggered safely against the real dependency.

Choose the lightest faithful option: fake, stub, simulator, local service, contract fixture, or mock. Verify the double's shape against the owned contract. A production adapter plus a test adapter can justify an internal seam, but it does not require exposing that seam to every caller.

Avoid doubles that encode internal call order or duplicate production branching. If the double needs complex conditional behavior, a local substitute or contract-level fixture may provide a more honest test.

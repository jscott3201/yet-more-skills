---
name: python-api-typing
description: "Design or review Python public APIs, typing, exceptions, and stubs. Use for semantic interface changes and SDK contracts, not formatter churn or native ownership alone."
license: MIT OR Apache-2.0
---

# Python APIs and Typing

Begin with callers and the supported Python versions, not a preferred typing style. Follow the existing type checker and its settings; Ruff is not a substitute for type analysis. Avoid installing several checkers or migrating the whole repository for one change.

## Design the contract

Make return shape, mutability, optionality, exceptions, sync/async behavior, and lifetime clear. Use Protocol for a useful structural seam, TypedDict for an appropriate mapping shape, and a dataclass or small class for behavior-bearing values. Type annotations do not validate runtime input. Use validation at the actual trust boundary; do not sprinkle casts or Any over a broken interface.

Distinguish missing values from explicit None and domain sentinels. Avoid mutable default arguments and mutable state accidentally shared between instances. A frozen dataclass is not deep immutability. Prefer accepting the narrowest useful behavioral interface without promising operations the implementation does not support. Document generator consumption, lazy errors, and one-shot resources.

Keep exception classes stable and actionable. Preserve causes when translating errors, avoid swallowing cancellation, and do not leak credentials in repr, logs, or diagnostic strings. Use explicit context-managed cleanup rather than relying on destructor timing.

## Keep the shipped surface honest

Update Python source, extension signatures, docstrings,.pyi files, exports, examples, and tests together when their contract changes. A native method returning an asyncio Future is an Awaitable, not necessarily a coroutine accepted by create_task or asyncio.run. Represent that distinction in stubs and exercise it as a consumer.

Generated stubs are candidates for review, not authoritative semantics. Check keyword-only and positional parameters, defaults, exception behavior, overloads, nullability, submodule imports, and context-manager methods. `inspect.signature` is not available for every native symbol; absence is not proof of a broken method. Use actual calls plus the configured checker.

Type syntax must parse on the supported floor, including distributed stubs. Do not adopt newer generic syntax or standard-library helpers merely because the author's interpreter supports them. Review runtime annotation consumers before changing annotation evaluation or moving imports behind TYPE_CHECKING.

## Evidence

Run a small external consumer against the installed package and its installed type information. Include at least one rejected invalid use and one accepted intended use. Keep expected-error annotations narrow; never silence the whole module to get a pass. Report runtime and static results separately.

Read [API checks](references/contracts.md) for mixed-language and domain examples.

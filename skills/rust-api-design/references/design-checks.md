# API design checks

For a borrowed decoding API, determine whether the caller can retain the backing frame. For a background task, owned request data or a deliberate shared buffer may be necessary. Returning a borrow into a mutable scratch buffer would constrain the next receive; make that tradeoff explicit.

For a persistence facade, avoid exposing a lower-layer type merely because it is convenient today. Ask whether it freezes representation, allocator, runtime, serialization, or error policy. A runtime-independent core should not acquire Tokio just because one consumer is asynchronous.

For public changes, distinguish source compatibility, trait/auto-trait compatibility, behavioral compatibility, and serialized compatibility. Adding a private-looking field to a public struct or changing `Send`/`Sync` behavior can affect consumers. Use the project's public-API checks when present; no one tool proves all these dimensions.

For error conversion, preserve protocol exception identity and database domain codes. A pretty string is not a replacement for a discriminant that downstream code uses to decide whether a retry is valid.

Sources: [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/), [Cargo compatibility reference](https://doc.rust-lang.org/cargo/reference/semver.html), [dyn compatibility](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility).

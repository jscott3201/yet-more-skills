# Tool limits and local policies

The Rust Reference lists undefined behavior and evolving areas of the memory model. Avoid overstating a complete formal model where the language documentation is still qualified. A test suite cannot enumerate all callers of a safe public API. [Undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html).

Miri interprets supported Rust execution to detect many UB classes. It is useful for a small unsafe abstraction and its safe callers; unsupported FFI, environment interactions, and unexecuted paths limit conclusions. Follow the project's selected nightly/component policy and current Miri instructions instead of installing or changing the stable compiler silently. [Miri](https://github.com/rust-lang/miri).

Native sanitizers observe instrumented executions and have platform/toolchain restrictions. Select them for a specific memory/race failure model; do not add every sanitizer to PR CI. [Rust sanitizers](https://doc.rust-lang.org/unstable-book/compiler-flags/sanitizer.html).

For foreign calls, reason about ABI, ownership, exception/unwind rules, and callbacks together. Prefer version-matched bindings and the foreign library's documented threading contract. [Rustonomicon FFI](https://doc.rust-lang.org/nomicon/ffi.html).

Preserve repository bans on unsafe code and the documented scope of any generated FFI exception. An exception at one boundary does not apply across the workspace.
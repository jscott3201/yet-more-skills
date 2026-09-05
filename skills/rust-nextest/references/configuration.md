# Configuration and version checks

A config is an executable policy, not just TOML. Successful parsing with a generic TOML library does not establish nextest schema support, matching filters, or effective runtime behavior.

Check that every configured key is supported by the enforced runner minimum. A newer option with an older declared floor is a compatibility risk, not proof that current CI is failing. Align the configuration and actual installation path deliberately.

Preserve existing flake, leak, timeout, and JUnit controls when adapting configuration examples.

When adjusting a config, check CLI and environment overrides, per-test overrides, and inheritance. Inherited JUnit report names are not proof of different output files: inspect resolved output locations, especially for concurrent runs or custom shared stores.

For selective concurrency, a group declares a budget and matching per-test overrides assign tests to it. A group of one prevents overlap only for its members inside that run. It does not lock a serial device against another process. `threads-required` accounts for scheduler capacity; it does not change how many OS threads the test creates.

Prefer adjusting a measured problematic test over enlarging timeouts globally. Keep a run-level bound in addition to per-test bounds where supported. Avoid silently ignoring warnings, overriding version checks, or retrying until green.

Sources: [repository profiles and inheritance](https://nexte.st/docs/configuration/), [config reference](https://nexte.st/docs/configuration/reference/), [test groups](https://nexte.st/docs/configuration/test-groups/), [heavy tests](https://nexte.st/docs/configuration/threads-required/).

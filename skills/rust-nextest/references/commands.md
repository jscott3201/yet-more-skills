# Nextest command recipes

Examples below assume an existing lockfile and discovered package names. Reuse repository scripts in preference to these illustrations. Read installed help for supported flags. Listing may compile tests; it is not guaranteed to be cost-free.

## Focused Modbus example

```bash
cargo nextest list -p example-client --locked -E 'test(transaction)'
cargo nextest run -p example-client --locked \
  -E 'test(transaction)' --no-tests=fail
cargo test -p example-client --doc --locked
```

Check the listing; a source module name is not a promise that test names contain that substring. Features must match the relevant caller and be carried into all commands.

## Broader consumer selection

```bash
cargo nextest list --workspace --locked \
  -E 'rdeps(example-codec)'
cargo nextest run --workspace --locked \
  -E 'rdeps(example-codec)' --no-tests=fail
```

`rdeps` includes the matched package and transitive reverse dependencies among the packages available to the test build. It does not include external repositories, excluded workspace packages, Python tests, or doctests. Run their checks separately when impacted.

## Optimized test execution

```bash
cargo nextest run -p example-client --locked --release \
  --profile ci --no-tests=fail
cargo test -p example-client --doc --locked --release
```

Use `ci` only where the repository defines it. Do not assume a profile called `ci-release` implies release compilation; inspect the wrapper command.

## Existing repository routes

Inspect the repository's documented local test and CI mirror scripts. Do not transplant gate paths or profiles from another repository.

Sources: [running tests](https://nexte.st/docs/running/), [filtersets](https://nexte.st/docs/filtersets/), [listing](https://nexte.st/docs/listing/), [Cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html).

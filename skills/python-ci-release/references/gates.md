# Gate decisions

A useful light lane answers whether the changed behavior and nearby contracts still work. A release lane answers whether the supported product can be built, installed, imported, and exercised on promised native targets. They are not interchangeable green badges.

For a mixed Rust/Python repository, enumerate Rust workspace tests, doctests, excluded binding crates, Python tests, and artifact checks separately. nextest does not run Python tests. Successful Rust tests do not establish Python signatures, cancellation, import packaging, or GIL-disabled execution. Successful editable Python tests do not establish sdist completeness.

Choose minimum and current supported Python deliberately; add a free-threaded variant only with its native dependency compatibility and real post-import GIL evidence. A prerelease interpreter is exploratory unless project policy says otherwise. As of this research date Python 3.15 is prerelease; no general skill forces projects to drop 3.11 or move to 3.15.

Use xdist only after fixture ownership is understood. A session fixture is per worker, and fixed protocol ports or single-writer database directories require allocation/isolation or serial execution. Avoid converting a benchmark into a mandatory noisy per-PR threshold without stable host evidence.

These are command shapes, not a replacement CI configuration. Verify installed flags and local wrappers. Existing workflows remain the authority.

Primary references: [pytest good practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html), [pytest exit codes](https://docs.pytest.org/en/stable/reference/exit-codes.html), [Ruff linter](https://docs.astral.sh/ruff/linter/), [maturin distribution](https://www.maturin.rs/distribution.html), [Python 3.15 schedule](https://peps.python.org/pep-0790/).

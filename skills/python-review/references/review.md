# Review examples

A strong finding names an input and path: a cancellation is caught and converted to success while a write remains active; an installed module comes from the source tree rather than the tested wheel; a `.pyi` declares a Coroutine while the actual callable returns an asyncio Future; an integer identifier crosses f64 and loses precision contrary to the documented identifier contract.

A weak finding says that an owned conversion could be zero-copy, that a small loop should become NumPy, or that a static annotation would be more elegant without proving a behavioral or maintainability problem. Escalate data loss, crash, deadlock, unsafe aliasing, or false validation claims above optional style changes.

Fixed benchmark ports require coordination across runs; they do not by themselves prove a product concurrency bug. Evaluate explicit sentinel and timezone conversion choices against the domain contract rather than declaring every non-generic conversion a defect.

For a report, use a short narrative or a small table. Commands that were not executed remain unrun. Do not re-run unchanged expensive suites simply to add activity; reuse valid evidence for unchanged relevant inputs under the repository's review policy. Do not impose new revision ledgers or model settings.

Primary references: [asyncio task cancellation](https://docs.python.org/3.14/library/asyncio-task.html), [pytest good practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html), [typing distribution](https://typing.python.org/en/latest/spec/distributing.html), [PyO3 types](https://pyo3.rs/v0.29.2/types).

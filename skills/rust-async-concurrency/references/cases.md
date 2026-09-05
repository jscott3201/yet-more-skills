# Concurrency cases

**A deadline scheduler:** Store absolute per-attempt deadlines. Wake when a nearer deadline arrives; avoid polling an entire structure periodically without a measured reason. Test an earlier insertion while the scheduler sleeps, stale timer events, and exact expiry/completion races. Choose capacity from the actual admission contract.

**A channel-based actor:** Bound queued work and document dropped receiver/sender behavior. Owning I/O in one task simplifies state ownership but can create a bottleneck; measure service time and head-of-line blocking before sharding it. [Tokio shared state](https://tokio.rs/tokio/tutorial/shared-state).

**A cancellation branch:** Review the concrete async method, not just the trait name. Some read/write convenience methods may have made partial progress when dropped. Use stateful operations or preserve progress when necessary. [Tokio select cancellation safety](https://docs.rs/tokio/latest/tokio/macro.select.html).

**A blocking worker:** Distinguish cancellation of a task that has not started from one already executing. A timeout waiting for it does not stop native CPU or I/O work. [spawn_blocking](https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html).

**A shutdown test:** Admit work, begin shutdown, attempt new admission, complete some work, hold other work past the deadline, and assert task/resource cleanup. Keep the operation's actual drain policy as the expected result. [Tokio graceful shutdown](https://tokio.rs/tokio/topics/shutdown).

**An ordering model:** Use Loom's synchronization types for the modeled section and account for code outside its instrumentation. Keep the model small enough to explore; document bounded schedules and complementary runtime tests. [Loom](https://docs.rs/loom/latest/loom/).

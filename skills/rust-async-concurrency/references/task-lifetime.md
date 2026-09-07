# Spawned task lifetime

Tokio JoinHandle owns the ability to observe a spawned task, not an automatic cancel-on-drop guarantee. Dropping it detaches the task. A timeout around an owned handle drops that handle when it expires; the spawned task may continue holding resources or producing effects.

Keep the handle with the lifetime owner when the owner must cancel and observe termination. A timeout around a mutable borrow of the handle can leave the handle available for the owner's next action. Choose cooperative cancellation for graceful work, or abort when the contract permits abrupt cancellation, then observe the join result. Completion can race cancellation; preserve that distinction. Abort is a request, not a synchronous cleanup barrier.

JoinSet has different drop behavior: dropping the set aborts its contained tasks. That does not make a dropped set a graceful drain or prove that every external effect was rolled back. A started spawn_blocking task cannot be aborted by treating its handle like an ordinary async task. Keep a cooperative stop path or an explicit documented limit.

Test an operation blocked on a controlled event, timeout or drop its caller, and observe whether the child still runs. Assert permit/registration recovery and the intended join outcome rather than merely asserting that timeout returned. Use an outer test deadline to keep a regression from hanging indefinitely.

Sources, checked September 7, 2026: [Tokio JoinHandle](https://docs.rs/tokio/latest/tokio/task/struct.JoinHandle.html), [Tokio JoinSet](https://docs.rs/tokio/latest/tokio/task/struct.JoinSet.html). Check the runtime actually used; do not generalize Tokio semantics to every executor.

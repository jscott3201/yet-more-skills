# Construction and failure cases

With ordinary scheduling, code after create_task often runs before the coroutine body. An eager task factory can instead run that body during construction. Python added asyncio.eager_task_factory in 3.12 and create_task's eager_start argument in 3.14; inspect the actual interpreter and configured factory rather than passing unsupported arguments.

A useful regression has two paths: the coroutine returns immediately from cached data, or suspends on an explicit event. Both must observe initialized owner state, release registrations, and surface failures. Do not rely on a sleep to make initialization win a race or change the process-wide task factory inside a library to force one ordering.

For default gather, a child's first exception is propagated while other children can continue. Cancelling a gather object after it is already done is not a reliable way to stop those children. Retain and supervise the tasks or choose TaskGroup when sibling cancellation and grouped errors are the intended contract. Test that the sibling's cleanup actually runs; receiving an exception in the parent is not that evidence.

Source, checked September 7, 2026: [asyncio tasks, TaskGroup, gather, and eager execution](https://docs.python.org/3/library/asyncio-task.html). These cases select tests; they do not authorize an interpreter or concurrency-framework migration.

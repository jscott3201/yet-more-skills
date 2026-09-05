# Async failure cases

Trace create -> admit -> send -> complete -> release -> close. For each boundary ask who can cancel, who owns the handle, and whether the action can already have an external effect. Use one recorded request identity through retries and cancellation. Do not add a second unrelated semaphore in Python if the native client already owns logical admission unless a separate bound is intentional.

A native function may return a Future immediately. `asyncio.create_task` expects a coroutine; await the result directly or use a coroutine wrapper when task ownership is required. Do not change a stub to Coroutine merely to quiet a checker.

Loop shutdown is not application shutdown. Close clients and await their work before closing the loop. Handle cancellation while __aexit__ runs, and preserve the primary exception without silently losing a cleanup failure. To expose timing defects, enable asyncio debug diagnostics in a focused run rather than a performance benchmark.

Use the installed pytest-asyncio loop_scope support, and keep fixture loop lifetime compatible with resources. An async fixture cached for a whole module must not hand out a client tied to a loop already closed by a prior test.

Primary references: [asyncio tasks and cancellation](https://docs.python.org/3.14/library/asyncio-task.html), [asyncio development and threads](https://docs.python.org/3.14/library/asyncio-dev.html), [asyncio runners](https://docs.python.org/3.14/library/asyncio-runner.html), [pytest-asyncio](https://pytest-asyncio.readthedocs.io/en/stable/concepts.html).

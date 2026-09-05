# Worker checks

Python 3.14 changed the default on supporting POSIX platforms from fork to forkserver; macOS retains spawn as its normal default. The practical instruction is to inspect the actual context and test it, not to hard-code one platform assumption into a reusable library. Resources created in one context can be incompatible with another.

Choose one overall CPU budget. Four Python workers each calling into a full-size Rayon pool and a threaded BLAS library can heavily oversubscribe a host. Measure the boundary workload with native inner parallelism and outer Python parallelism as separate alternatives. Do not mutate process-wide thread environment settings without agreeing their scope.

Free-threaded Python has runtime and extension constraints beyond the interpreter filename. It also has context-inheritance behavior that differs from ordinary builds. Pass application context intentionally, especially for request IDs, credentials, and cancellation; do not rely on defaults being equal across build variants.

Use isolated processes when testing interpreter exit, aborts, native panics, or leaked threads. A killed subprocess provides failure evidence, not proof of cleanup. Test both graceful completion and forced failure where the product contract calls for it.

Primary references: [multiprocessing contexts](https://docs.python.org/3.14/library/multiprocessing.html#contexts-and-start-methods), [executors](https://docs.python.org/3.14/library/concurrent.futures.html), [threading](https://docs.python.org/3.14/library/threading.html), [free-threading guide](https://docs.python.org/3.14/howto/free-threading-python.html).

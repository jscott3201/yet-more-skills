# Async failure cases to reproduce

## Site switch during a request

Request A starts for site A. The operator switches to B; request B completes. A then completes.
Correct behavior is not merely “A was aborted”: the response acceptance path and cache identity
must prevent A from becoming B's displayed data even when the transport ignores cancellation.
Repeat during logout/login, search-query changes, and closing/reopening an editor.

When using TanStack Query, keep all resource-defining inputs in the query key and consume the
supplied AbortSignal in the transport where supported. Follow the actual version's behavior;
unmounting alone does not guarantee the underlying promise was cancelled. Mutation completion
may still need reconciliation after its original component unmounts.

## Streaming telemetry

The classic browser WebSocket API does not provide automatic backpressure. Choose bounded
retention and document which updates may be replaced by a newer sample. Present dropped or
missing-data evidence when the contract requires it. Limit reconnects with backoff and a
terminal or operator-visible unavailable state. Clear prior-context data before resubscribing.

Avoid triggering a component update for every high-frequency raw event. Batch rendering at
an appropriate cadence without changing persisted evidence or pretending that interpolated
data is a source observation. Ensure background tabs and slow consumers cannot grow memory
indefinitely.

## Workers and transfers

Treat worker messages as an API: validated request kind, task identity, bounded payload,
result/error outcome, and disposal. Transferable ArrayBuffers relinquish ownership at the
sender; choose copying where continued ownership is required. A terminated worker may not
complete cleanup that the UI expects, so the parent owns its visible pending state.

## Cleanup matrix

Test success, validation failure, network failure, timeout, explicit cancellation, context
change, unmount, and repeated start/stop. Verify no duplicate listeners or reconnect loops.
Detach only resources owned by the current instance; broad global cleanup can break another
panel or agent test server. Restore fake clocks and global mocks after the test.

## Sources

Use documentation matching the installed version.

- [Query cancellation](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation)
- [Query keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys)
- [Web workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
- [WebSocket limitations](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

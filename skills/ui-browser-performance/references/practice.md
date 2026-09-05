# Product-shaped performance experiments

## Large equipment list

Compare initial load, applying a filter, opening a detail panel, switching sites, and returning
to the list. Inspect payload size, parsing, sorting/filtering, mounted DOM, and retained caches
separately. If the server sends too much data, rendering virtualization alone will not solve
the network or retained-memory problem.

## Long-running telemetry view

Leave the view active under representative update rates and repeat subscription changes.
Inspect memory growth, retained listeners, worker queues, and CPU while hidden/backgrounded.
Batching display updates may help, but preserve the original timestamps and the domain's gap
and audit requirements. A queue cap without an explicit overflow policy can silently corrupt
the meaning of the UI.

## Interaction timing

INP is a field-oriented responsiveness metric with defined aggregation. A local browser trace
can reveal long tasks and slow rendering opportunities but is not itself the site's field INP.
Document a local click-to-visible-result measure as a lab measure. Keep API completion timing
separate from presentation timing and from physical action completion.

## Bundle changes

Inspect what a supported production build emits and what the browser requests. Splitting a
heavy optional editor can improve startup, but additional request dependencies may delay the
first use. Compare the actual route workflow, not only the size reported by the bundler.
Account for caching and stale-chunk recovery during upgrades.

## Evidence without a benchmark bureaucracy

A useful report is the workload, environment, bottleneck, change, repeated results, tests,
and remaining unknowns. Keep raw traces only when they help explain the outcome. Do not add a
full performance CI matrix to every PR or claim a universal threshold based on one machine.

## Sources

Use documentation matching the installed version.

- [Interaction to Next Paint](https://web.dev/articles/inp)
- [Web workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
- [WebSocket and backpressure](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [Vite build features](https://vite.dev/guide/features)
- [TanStack Virtual](https://tanstack.com/virtual/latest/docs/introduction)

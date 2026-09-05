# A focused React optimization pass

## Example: selecting a node stalls a large workspace

Capture the interaction and determine whether all nodes rerender, a global selector constructs
a new object on every store update, the inspector repeats a large transformation, or layout
work dominates. Avoid jumping straight to memoizing every node. Preserve the stable node
identity and keyboard selection contract.

A narrow selected-ID subscription can avoid waking unrelated consumers. A memoized expensive
derived view may help if its input identity is meaningful. If an external library recreates
every object, fix the update boundary rather than layering caches over unstable data. Validate
selection changes, deleted nodes, resource revisions, and retained drafts after the optimization.

## Bundle and network

Compare eager and lazy route behavior against the actual workflow: making the first critical
operator screen wait for a chart chunk may be worse even when the initial bundle shrinks.
Identify independent requests and start them together within service limits. Do not adopt a
new data-fetching library just because an upstream React skill uses it in examples.

## Compiler-aware review

Find the compiler configuration instead of inferring it from React's version. A compiler
upgrade or enablement is its own scoped change with relevant regressions and measurements.
Keep intentional memoization that protects external API identity until evidence shows a safe
replacement. Do not use memoization as correctness-critical storage: state and refs own that.

## Useful comparison record

Record the user operation, dataset shape, build mode, browser/device, measured bottleneck,
change, repeated results, and correctness checks. A few clear sentences or a small table are
enough. CPU throttling helps reproduce conditions but does not prove performance on every
field device. Report a local interaction timing as a lab result, not an actual field INP score.

## Sources

Use documentation matching the installed version.

- [React Compiler](https://react.dev/learn/react-compiler)
- [React guidance on avoiding unnecessary effects](https://react.dev/learn/you-might-not-need-an-effect)
- [React Flow performance](https://reactflow.dev/learn/advanced-use/performance)
- [Interaction to Next Paint](https://web.dev/articles/inp)

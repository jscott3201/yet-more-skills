# Context efficiency: research and decisions

Reviewed September 7, 2026. This is an on-demand reference for efficiency investigations, not a required preflight for ordinary coding.

## What changes behavior here

The existing collection already discourages generic architecture surveys and mandatory orchestration. The remaining opportunity is to turn that intention into a usable sequence: start from the known owner, resolve a specific uncertainty, retrieve enough to interpret it correctly, and stop that exploration when the decision is supported. Large tasks still deserve broad coverage; they need focused subquestions, not a smaller unannounced deliverable.

Three costs need separate treatment: metadata exposed during skill/tool discovery, bodies and evidence loaded during work, and total agent-loop work including repeated reasoning, retries, validation, and workers. Optimizing only the final answer or one tool response misses the other costs. This update adds one specialist, embeds inexpensive defaults in existing entry points, and narrows the existing catalog-list command. It does not introduce a second runtime or an always-on context accountant.

## Libraries and skill collections inspected

| Source | Useful mechanism | Decision for this collection |
| --- | --- | --- |
| [RTK](https://github.com/rtk-ai/rtk) | Command-specific output reduction with raw-output recovery | Adopt compact observations with exit status and a retrievable source. RTK remains optional; filters must not hide failures or change command semantics. Its advertised savings are not whole-session measurements here. |
| [Serena](https://github.com/oraios/serena) and its [evaluation notes](https://oraios.github.io/serena/04-evaluation/030_results/010_cc_on_tianshou.html) | Symbol-aware retrieval and references instead of entire files | Use an already available semantic navigator for an implicated symbol; verify coverage and invariants. Do not set up an index to answer a trivial question or replace a one-line patch with an unnecessarily large symbol rewrite. |
| [Context Mode](https://github.com/mksglu/context-mode) | Processing large observations outside model context, returning selected data, and retrieving indexed evidence | Adopt filtering before ingestion and references for follow-up. Do not adopt compulsory routing hooks, session databases, or a universal code-execution proxy. An isolated subprocess is not automatically a full security sandbox. |
| [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-optimization/SKILL.md) | Separates caching, masking, compaction, and partitioning | Keep the distinctions. Do not import fixed utilization thresholds, cache-hit targets, or reduction percentages without local measurement and runtime support. |
| [bm629 token-optimization](https://github.com/bm629/agent-skills/blob/main/skills/token-optimization/SKILL.md) | Treats cost across a completed task rather than one prompt | Include retries and worker overhead in evaluation. Do not turn its broad tactic catalog into another long mandatory loading step or automatically switch models. |
| [Codex Token Optimizer](https://github.com/HelloWorld668/codex-token-optimizer) | Distinguishes shell-output reduction from broader context compression and warns about measurement scope | Keep dependencies optional, retain decisive raw evidence, and do not report reducer statistics as the user's overall savings. No third-party runtime was installed or benchmarked in this pass. |

These are original workflow changes informed by public descriptions and selected documentation, not imported implementations or a security audit of those tools. Existing licenses and adaptation notices elsewhere in the collection are retained.

## Primary guidance and research

[OpenAI's skills documentation](https://developers.openai.com/codex/skills) describes progressive loading: initial names/descriptions, then the selected skill body. Its documented initial-list budget can shorten descriptions or omit entries in a large installation. Therefore shorter bodies alone do not solve catalog overhead. Focused installation and useful trigger descriptions matter; an explicit-only policy is an invocation choice, not a promise that its metadata consumes no context.

[Agent Skills authoring guidance](https://agentskills.io/skill-creation/best-practices) supports concise, actionable instructions and progressive disclosure. Keep failure boundaries close to the action they govern. Move optional depth behind links that name when to read it; do not hide essential authority or validation rules in an optional file.

[Anthropic's context-engineering guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) supports just-in-time retrieval, identifiers, and task-dependent context management. The adaptation here is a widening rule, not a fixed number of files: expand when the current evidence cannot support the next decision. Useful batching can be cheaper than an excessively fragmented read loop.

Three research leads were checked at their abstract/summary level, not reproduced:

- [The Complexity Trap](https://arxiv.org/abs/2508.21433), revised October 27, 2025, compares observation masking and model-generated summaries in specified coding-agent benchmarks. It motivates testing a simpler masking baseline before buying repeated summarization calls. It does not establish that old failures or instructions can safely be removed in every task.
- [SkillReducer](https://arxiv.org/abs/2603.29919), revised June 24, 2026, treats routing descriptions and body/reference disclosure as separate optimization layers with faithfulness checks. It motivates selective restructuring, not automatic deletion of every long paragraph.
- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) reports uneven benefits and substantial overhead for some injected skills in its evaluated tasks. It motivates comparing a task with and without a specialist, including whether the task actually matches. It is not evidence that this collection's changes improved solve rate.

## Runtime features are not prompt powers

A skill can change future retrieval and output choices. It cannot retroactively delete already-loaded observations, select an unavailable model, or make a host support deferred tool discovery. Use host-supported compaction or tool search only when available and authorized. A plain summary written into the same conversation may add tokens rather than remove any.

[Caching behavior is model- and API-dependent](https://developers.openai.com/api/docs/guides/prompt-caching). Keeping reusable prefixes stable can help, while rewriting history, compaction, or changing tool definitions can affect reuse. Cache reads, cache writes, retention, and reported usage vary. Do not hard-code a universal rate or use padding to chase cache hits. Caching changes compute/cost characteristics; it does not make irrelevant text absent from context. Prefer the smallest adequate input, then assess caching in the actual supported deployment.

Similarly, delegating a long read can shrink the coordinator's context while increasing total billed work. Use workers for independent questions or useful isolation, not as a reflexive token-saving trick. Do not attach every language specialist or an entire parent transcript to every child. Runtime/model changes need separate scope and evaluation.

## A proportionate comparison

Use a handful of representative real tasks: a local correction, a lifecycle bug, a cross-language change, a UI state bug, a broad research task, and a recovery after truncated evidence. Compare the previous and revised instructions with equivalent source, task, tools, model/settings, and success criteria. Include both explicit skill use and normal routing. Repeat uncertain cases enough to avoid treating one lucky response as a general result.

Judge correct completion, required checks, scope, and missed regressions first. Then inspect actual input/output usage, cache accounting, repeated reads, tool calls, retries, worker overhead, and latency where the host exposes them. Record no more than a short result note and the evidence already produced. Do not fabricate hidden usage; provider-reported reasoning tokens may already be included in output totals and must not be counted twice.

A character or byte count is a payload measurement, not a tokenizer count, bill, or guarantee of shorter reasoning. A smaller catalog response can be demonstrated deterministically; improved end-to-end cost and behavior require actual comparable agent runs. No such model comparison is claimed by the structural tests or authored scenarios in this update.

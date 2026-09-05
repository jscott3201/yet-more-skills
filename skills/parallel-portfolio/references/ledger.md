# Portfolio ledger

Read this reference when admitting or operating a parallel portfolio. Keep one compact record and update it only at real phase changes.

```text
PARALLEL_PORTFOLIO_LEDGER
portfolio ID and objective:
owner/repo and repository-local parallel authority:
target branch and common base SHA/tree:
Codebase Memory project/root and coverage:
integration branch/PR strategy and declared lane order:
shared frozen digests and exclusion zones:
lane 1: ID, outcome, branch/worktree, owned paths/symbols, prohibited paths/symbols, prerequisites, gates, status, commit/PR/review head
lane 2: ID, outcome, branch/worktree, owned paths/symbols, prohibited paths/symbols, prerequisites, gates, status, commit/PR/review head
combined gates and rehearsal:
integration head/tree and review state:
merge/close authorization:
unrelated WIP:
replan triggers:
next action:
END_PARALLEL_PORTFOLIO_LEDGER
```

Every writer dispatch must include:

```text
PARALLEL_LANE_PACKET
portfolio and lane IDs:
owner/repo, target branch, common base SHA/tree:
lane branch/worktree, current work HEAD/tree, and clean state:
Codebase Memory project/root and coverage:
objective and acceptance evidence:
owned paths and symbols:
prohibited paths, symbols, and shared zones:
frozen dependency/contract/lock digests:
independent prerequisites:
initial implementation or approved repair; confirmed finding IDs and cycle counters:
required lane gates (packet and repository policy):
combined gates explicitly deferred to integration and reason:
unrelated WIP:
replan triggers:
END_PARALLEL_LANE_PACKET
```

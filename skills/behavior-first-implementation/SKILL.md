---
name: behavior-first-implementation
description: Implement an authorized bounded change test-first through public behavior seams using vertical red-green-refactor slices. Use only during implementation when the user or brief calls for TDD; not for diagnosis-only or review work.
license: MIT OR Apache-2.0
metadata:
  compatibility: "Codex and OpenCode 1.x"
  upstream-repository: "https://github.com/mattpocock/skills"
  upstream-commit: "6654f6b60cd9d5be8b54c6fafe44346dabeb3b76"
  adaptation: "Bounded Codex/OpenCode workflow"
---

# Behavior First Implementation

Apply TDD inside an already authorized implementation lane. Consume the bounded brief, grounding record, acceptance evidence, scope, and ownership constraints. This skill never authorizes implementation, Git/GitHub actions, or a wider change surface.

## Choose the behavior seam

Identify the highest stable interface through which a caller can observe the requested behavior. Reuse repository test conventions and existing fixtures. Treat interface shape as settled when the brief and live source agree; if a public contract or seam remains materially unresolved, stop with `REPLAN_REQUIRED` rather than designing it implicitly.

Read [test-quality.md](references/test-quality.md) when choosing assertions or diagnosing a weak test. Read [test-doubles.md](references/test-doubles.md) when an external dependency needs substitution.

## Run vertical red-green-refactor cycles

For one behavior at a time:

1. **Red:** add the smallest test that expresses one acceptance behavior through the chosen seam. Run it and confirm it fails for the intended missing behavior. A test that already passes or fails during unrelated setup is not a red signal.
2. **Green:** make the smallest production change that satisfies that test without anticipating later slices. Run the focused test again.
3. **Refactor while green:** improve names, duplication, and local structure only within the bounded scope. Keep the focused test green after each meaningful change.
4. **Integrate:** run the nearest relevant package or subsystem checks before starting the next slice.

Repeat with the next observable behavior. Avoid writing a horizontal batch of speculative tests before the implementation has taught you what the next slice should be.

## Preserve test value

- Assert caller-visible outcomes, durable state transitions, emitted contracts, or externally observable failures.
- Derive expected values from the specification, a worked example, a trusted fixture, or another independent oracle—not by repeating the implementation algorithm in the test.
- Keep repository-native unit, integration, contract, or end-to-end boundaries when they already protect the behavior. “Highest seam” is guidance, not a reason to replace effective tests.
- Use test doubles at true system boundaries or to make nondeterminism controllable. Do not mock internal collaboration merely to mirror call structure.
- Add a regression test only when it can reproduce the real failure pattern. If no honest seam exists, return that as a design finding rather than adding a false-confidence test.

## Close the implementation lane

Run the focused acceptance command, the repository-required static checks, and one appropriate broader suite. Record compact results and verify the tracked change set remains within scope. Do not commit, push, publish, or self-approve review; return the worktree and evidence to the orchestrator or caller that owns delivery.

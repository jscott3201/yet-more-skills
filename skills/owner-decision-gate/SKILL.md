---
name: owner-decision-gate
description: Resolve material PR, milestone, contract, infrastructure, and authority choices with concise recommended user questions before implementation depends on them.
license: MIT OR Apache-2.0
metadata:
  category: delivery
  phase: decision
---

# Owner Decision Gate

Use this gate after enough grounding and bounded research exists to state a real choice, and before dependent work requires that choice. Questions remove material ambiguity; they do not replace inspection or delay already-authorized preparation. Merge approval belongs after the PR is reviewed and ready under `pr-gate-loop`, not before implementation.

## Ask when the answer changes the work

Follow the active harness's input-tool rules. Use asynchronous input for optional preferences and continue independent authorized work. For a required owner decision or permission request, use the mechanism the harness permits; if no suitable tool is available, ask one concise direct question and pause only dependent work. Do not switch modes to expose a tool. Ask when any of these remains unresolved:

- more than one coherent PR slice or milestone path is eligible and the choice changes sequencing, scope, or acceptance;
- a public contract, source owner, persistence model, irreversible migration, compatibility promise, or milestone exit condition has credible alternatives;
- the work would introduce or expand a provider, hosted service, credential, recurring cost, release/CI policy, destructive cleanup, security boundary, or external publication;
- the request, handoff, roadmap, live repository, or prior owner decision conflicts materially;
- success cannot be demonstrated without choosing among materially different acceptance targets;
- new authority is required, including merge approval when no valid standing approval exists.

Do not ask for facts that tools can discover, routine reversible implementation details, or a decision already recorded for the current scope. Use reasonable assumptions when alternatives do not materially change the requested outcome. Never re-ask an unchanged answer merely because a new PR began.

## Question contract

1. Complete already-authorized work needed to make the proposed action concrete and reviewable, including reversible preparation and validation. Do not perform work whose correctness depends on an unanswered consequential choice.
2. Batch related blockers at the earliest decision checkpoint. Ask one to three short questions, not a drip of follow-ups.
3. When using a choice tool, give two or three mutually exclusive choices with a recommended default and one-sentence tradeoffs. For direct questions, use the concise format permitted by the harness.
4. State the concrete scope, schedule, compatibility, cost, or risk consequence. Do not bury the recommendation in a status update.
5. Pause only work whose correctness or authority depends on the answer. Continue independent authorized work while waiting. For an optional unanswered preference, allow reasonable time and then state the assumption used; silence never grants permission or settles a consequential owner choice.
6. Record the answer in the orchestrator ledger. Persist it to the project roadmap or program repository only when that repository owns the decision and the current task authorizes the update.
7. Treat only an actual user reply as an answer. Tool approval, command approval, silence, prior preference outside its validity conditions, or a response to another question is not owner authorization.

At a user-declared milestone hard stop, summarize progress against exit criteria and ask whether to close gaps, enter the next milestone, or replan before dispatching another implementation.

## Compact record

```text
OWNER_DECISION_RECORD
context and evidence:
decision status: NO_DECISION_NEEDED | NEEDS_USER | RESOLVED
question and choices:
recommendation and tradeoff:
owner answer:
scope/acceptance/authority impact:
valid until:
END_OWNER_DECISION_RECORD
```

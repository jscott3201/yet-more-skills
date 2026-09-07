---
name: ui-agent-collaboration
description: "Design or review human-agent collaboration in an application: editable proposals, scoped approval, interruption, recovery, and accessible execution state. Not generic chatbot styling, tool-server authorization alone, or permission to execute proposed actions."
license: MIT OR Apache-2.0
---

# Human-Agent Collaboration UX

Design around the user's task, not around displaying a chat transcript. Inspect the real application capabilities, permission model, domain state, and execution events. Use the existing React, Svelte, or other UI conventions. Do not fabricate tools, backend endpoints, progress, or successful outcomes to complete a visual design.

## Keep people able to steer

Make the agent's scope and limitations visible where they affect the decision. Let users inspect, edit, reject, or apply a meaningful portion of a proposal without restarting the whole interaction. Preserve useful drafts and provide a non-agent route for core tasks when the product supports one. Do not make generated prose the only way to understand a proposed change.

Show the actual target, relevant evidence, differences from current state, and consequences before an impactful action. Distinguish a suggestion from a validated proposal and from an admitted operation. Use existing approvals; do not add confirmation to every harmless read or interpret a broad approval as permission for unrelated work.

## Make approval and state match

Bind an approval to the operation, scope, inputs, and resource revision required by the application's contract. Editing a proposal or changing site, account, permission, or relevant resource state may invalidate it. The trusted backend must enforce this; a disabled button or model promise is not authorization.

Use explicit observable states such as preparing, awaiting input, admitted, running, completed, failed, and outcome unknown as the real contract requires. Progress should come from actual work events, not simulated percentages or claims that the model has finished thinking. Provide a concise rationale and evidence when useful, not a fabricated internal reasoning transcript.

## Design interruption and recovery

Explain whether Stop prevents new work, requests cancellation, or actually reverses a completed change. A disconnected stream or closed panel is not proof that server work stopped. Reconcile uncertain effects through the operation's existing status path before offering Retry; keep the same operation identity when the backend contract requires it.

After reconnect or session change, restore only state the application can establish. Handle permission loss, partial completion, stale evidence, and unavailable tools without leaving an enabled action that cannot be performed. Keep human-facing and machine-readable operation state consistent, while applying the same access restrictions to both.

## Validate the collaboration

Test a user correcting a proposal, rejecting one part, switching context before approval, interrupting after admission, and returning after a lost connection. Test the important path with the agent unavailable. Verify keyboard access, focus continuity, restrained status announcements, and recovery from errors; streaming text must not steal focus or announce every token.

Report actual capabilities and observed interaction evidence. Source inspection is not a usability study, and a polished screenshot does not prove that approval or cancellation works.

Read [interaction cases and sources](references/interaction-cases.md) for a compact review exercise.

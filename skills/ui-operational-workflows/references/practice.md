# Product-shaped UI cases

## Fault investigation

A list item links an equipment identity, condition, evidence interval, and data quality. An
operator acknowledgement is workflow state; it is not proof the condition stopped. A suppressed
finding may remain active. A cleared condition may still require verification. Keep these
distinctions visible without overwhelming the default view with every audit field.

## Device or control write

The UI may send an intent that later encounters admission, execution, or readback uncertainty.
Label each outcome according to the actual contract. HTTP 200/202 alone does not establish a
physical change. After a timeout, use the existing status/reconciliation path when available;
otherwise state uncertainty and a safe recovery action instead of offering a blind repeat.

Browser cancellation only releases local ownership of waiting. It does not prove transport,
provider, or physical rollback. A command accepted under an earlier resource revision must not
appear as a confirmed action on a newly selected resource.

## Energy and trends

Show the metric's unit, interval, quality, and calculation basis where relevant. Missing data
is not zero consumption. Separate estimates from measured values and avoid presenting overlapping
or incompatible windows as an exact total. A display downsample should preserve a way to inspect
source evidence and gaps; do not claim reduced display data is a full-resolution archive.

## Configuration

Keep BACnet, Modbus, MQTT, and HTTP driver configuration visually consistent without pretending
they share identical semantics. Preserve protocol-specific fields and limits from the backend
contract. Validate local syntax for prompt feedback, then show authoritative server errors and
connection/test outcomes separately. Do not treat a successful form save as device qualification.

## Scope of this guidance

These are UI safeguards, not claims of BACnet,
Modbus, ASHRAE, or safety certification. Protocol conformance remains a separate source-grounded
engineering task. Use the current repository state for implemented capabilities and rules.

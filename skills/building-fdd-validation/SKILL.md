---
name: building-fdd-validation
description: Implement or review building fault-detection logic against point quality, units, equipment modes, time windows, and independent fault scenarios. Not UI styling, compliance certification, or physical-control authorization.
license: MIT OR Apache-2.0
---

# Building FDD Validation

Start from the actual rule definition, equipment model, and authoritative sequence or specification supplied for the task. The checklist below is engineering guidance, not a substitute for an ASHRAE clause, protocol standard, or validated plant model.

## Establish when evaluation is meaningful

Map required points, semantic meaning, units, sign conventions, source identity, sampling assumptions, and quality states. Keep missing, invalid, stale, unavailable, and known zero distinct. A numeric input is not automatically usable evidence. Inspect operating mode, enable conditions, occupancy or schedule, commanded versus observed state, and sensor plausibility as the rule requires.

Separate “not evaluated” from “evaluated and normal.” Do not turn missing samples into a healthy result, fill a long data gap by interpolation without a contract, or compare incompatible time windows and units. Preserve provenance so an operator can trace a finding to the evidence used.

## Make temporal behavior explicit

Inspect threshold direction, hysteresis, persistence duration, startup/transient exclusions, reset conditions, suppression, and recovery. Define behavior across out-of-order samples, clock changes, process restart, mode changes, and data gaps. Use deterministic event-time fixtures rather than long sleeps.

Do not invent universal thresholds or timers from a similar piece of equipment. Follow the versioned rule/sequence and surface an unresolved domain choice. Acknowledging or suppressing a finding does not prove the equipment recovered.

## Validate independently

Exercise a normal trace, a clear fault, a near-threshold trace, unavailable evidence, a mode transition, and recovery. Derive expected outcomes independently from the implemented algorithm. Test the rule's preconditions as well as its inequality. For interconnected equipment, verify which asset and evidence own the finding; avoid multiplying one root cause into misleading independent counts.

For learned detectors, protect evaluation from time/site leakage and report the labeled scope, false alarms, missed faults, and uncertainty actually measured. Synthetic traces are useful regression evidence, not proof of field performance.

Energy or emissions impact requires a defensible baseline, units, time horizon, and avoidance of double counting. Never fabricate savings to populate a demo. Keep findings advisory unless an authorized control workflow explicitly accepts them.

Return preserved semantics, exercised scenarios, observed outcomes, and the specific specification or field-validation gaps.

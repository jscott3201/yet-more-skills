# Protocol boundary examples

**Advertised capacity:** A configured number and the promise representable on the wire may differ. Preserve sentinel meaning and test values between encoding steps. Verify the applicable specification before changing normative interpretation.

**Destination provenance:** Keep link-layer destination provenance distinct from effective network destination. Combining them can change routed traffic behavior.

**Bounded correlation:** A transaction ring still needs full request identity and expected response fields. Preserve validation during lookup and cleanup optimizations.

**Serial evidence:** Raw frame/CRC fuzzing and timestamped assembler fuzzing answer different questions. Include timing boundaries and stale tokens; a byte-only harness does not establish driver timing behavior.

**Source selection:** Follow repository navigation for licensed specifications. Public Modbus documents can be located through the [Modbus specifications page](https://www.modbus.org/modbus-specifications). Verify the edition and actual clause text; this skill is not a normative protocol reference.

# Domain examples

The reviewed Haystack converter checks bool before numerics, rejects a raw datetime in favor of its timezone-aware domain wrapper, and retains distinct marker types. Its native time-to-Python path converts nanoseconds to microseconds. These are points to test and document, not automatic findings that the implementation is wrong. Precision requirements belong to the API contract.

Useful adversarial examples include `2**53 + 1` converted through float, `True` passed as a register quantity, a null JSON field versus an absent key, an offset-preserving timestamp with a different source zone, and a nested list that is small in bytes but expensive to visit repeatedly. Each expected result must come from the domain policy, not from whatever the current implementation returns.

For strict JSON output, `allow_nan=False` rejects non-finite float values. Input requires its own policy: `parse_constant` can reject NaN/Infinity tokens and `object_pairs_hook` can detect duplicate names. Neither alone establishes full domain validity, Unicode interoperability, or bounded parser resource use. Do not advertise sorted keys plus compact separators as a formal canonical-JSON algorithm; normalization, numbers, and Unicode have additional requirements.

Native wrappers should retain quality flags, units, identifier identity, and stable exception categories. Do not embed BACnet or Modbus wire logic in a Python wrapper when the Rust codec already owns it. Shared-core round trips prove bridge consistency; independent reference vectors test the underlying semantics.

Primary references: [JSON behavior](https://docs.python.org/3.14/library/json.html), [datetime](https://docs.python.org/3.14/library/datetime.html), [numeric type relationships](https://docs.python.org/3.14/library/stdtypes.html).

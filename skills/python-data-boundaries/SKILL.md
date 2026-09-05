---
name: python-data-boundaries
description: "Use for Python serialization, numerical conversion, timestamps, units, missing values, or untrusted data entering protocol, building, and storage APIs. Not a generic dataframe or schema-framework migration."
license: MIT OR Apache-2.0
---

# Python Data Boundaries

Preserve meaning at Python, wire, and native boundaries. Read the actual domain contract before choosing coercion, normalization, or rejection. A shorter representation is not automatically equivalent.

## Define the value domain

Identify accepted Python types, encoded representation, Rust destination types, and round-trip expectations. Distinguish absent, explicit null, false, zero, empty, unavailable, and domain sentinels such as Haystack Marker/NA/Remove. Do not use truthiness to select a default when zero or false is valid.

Check subclass relationships before conversion: Python bool is an int subclass and datetime is a date subclass. Decide whether subclasses and objects with conversion methods are accepted; conversion can execute Python code. Keep protocol ranges and maximum collection sizes explicit. Python's arbitrary-size integers do not fit every Rust integer, float, timestamp, or wire field.

For numeric values, test exact integer boundaries, values beyond binary64's consecutive-integer range, signed zero, NaN/infinity, overflow, and rounding. Preserve units and scale with the value. Do not silently convert engineering units, truncate timestamps, or use an epsilon where byte/bit determinism is the contract. Approximate numerical comparisons need a justified tolerance and separately tested exact/discrete cases.

## Treat time as data with a policy

Separate wall-clock timestamps from monotonic deadlines. Define timezone awareness, UTC normalization, source zone retention, ambiguous/nonexistent local times, and supported resolution. Test DST folds, offsets, pre-epoch times, and conversion overflow. Do not infer an IANA zone from a numeric offset or silently interpret naive datetimes as local time.

For historian and protocol data, preserve quality/status flags and observation versus ingestion time. Missing samples are not zero measurements. Sorting, duplicate resolution, and aggregation need explicit policies rather than accidental dict or floating-point behavior.

## Bound and validate serialization

Enforce input byte/element/depth budgets at the appropriate layer before expensive work. Python's JSON defaults are not a strict domain validator: non-finite tokens and duplicate names need deliberate handling. Distinguish JSON syntax acceptance from schema and application validity. Do not deserialize untrusted pickle or execute arbitrary objects to interpret a data file.

Use independent examples for wire/JSON compatibility, including Unicode and malformed encodings. A Python-to-Rust-to-Python round trip through the same converter is useful but cannot by itself detect shared coercion mistakes. Keep conversion ownership explicit and measure copies before removing them.

Report the preserved contract, intentional losses or rejections, boundary tests, and compatibility implications. Do not replace a repository's chosen schema library solely to satisfy this skill.

Read [domain examples](references/domains.md) when touching building or native data.

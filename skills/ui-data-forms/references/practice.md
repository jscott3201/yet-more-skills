# State ownership examples

## Filtered equipment list

The URL can own navigable filters and sort choices. The query owns returned rows. Selection
is keyed by stable equipment identity, not current row position. The form owns the editable
fields of the selected equipment. Decide whether selection survives filters and make bulk
scope explicit; “all selected” must not silently mean all equipment in a site.

Query keys should represent the actual request inputs. Never use only a friendly label such
as `equipment` when the result also depends on site and time range. Clear or retire state on
principal changes according to the security model, not merely on component unmount.

## Configuration save

Keep the source revision with the draft. A save that conflicts with a newer server revision
needs a visible resolution path, not silent last-writer-wins. A timeout after submission may
have an unknown remote outcome; use the existing operation identity/status lookup if available.
Do not solve uncertainty by issuing a fresh write automatically.

For safe reversible metadata edits, an optimistic view can be appropriate. Define rollback,
concurrent mutation ordering, and post-confirmation reconciliation before using it. A device
command or irreversible deployment requires the domain's actual confirmation path instead.

## Validation

Separate formatting, parsing, local field validity, cross-field validity, and server rejection.
Unit conversions must preserve the original domain precision and supported range. Explain
constraints beside the field rather than in a generic toast after failure. Keep errors tied
to the exact submission, and clear obsolete errors when they no longer describe the draft.

## Loading and failure copy

Loading, no matching results, no configured assets, unavailable service, and forbidden access
are different screens. Preserve this distinction even when the API wrapper returns a single
error object. A stale successful result during a failed refetch is not current data; make its
timestamp/quality visible without unnecessarily erasing still-useful context.

## Sources

Use documentation matching the installed version.

- [TanStack query keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys)
- [TanStack query cancellation](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation)
- [Optimistic update tradeoffs](https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates)

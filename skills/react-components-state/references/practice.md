# State and composition decisions

## Asset editor

The query cache owns the last confirmed asset. The editor owns its unsaved draft. A new server
response must not blindly overwrite a dirty draft. On a resource identity change, decide
whether to discard, retain, or confirm the draft; do not let state from asset A become asset B's
input by accident. A validation error belongs to the submission it describes.

A derived count or filtered array usually does not require an effect plus a second state
variable. A socket subscription or an imperative map does require synchronization and cleanup.
A save request normally belongs to the save interaction, not an effect watching a `shouldSave`
flag. These choices reduce possible race states without adding another state-management layer.

## Effects under changing inputs

Check the values captured by the callback and the identity of the external resource. Cleanup
the resource created by that run, not whatever happens to be in a mutable global variable.
Ensure a second setup does not create duplicate connections or event handlers. Do not use
refs merely to hide an undeclared reactive dependency; use them for genuinely non-render state.

## Composition without abstraction inflation

A settings panel may share a field label, description, error region, and control. Keep those
as coherent local components. A compound component is useful when parts cooperate through one
interaction contract; it is not automatically better than ordinary props. Inspect consumer
readability and testability before introducing a provider or generic slot framework.

## Framework separation

Recommendations about RSC serialization, `next/dynamic`, server actions, or request-local
React caches require the relevant runtime. They do not become valid in a Vite SPA because
React is installed. React's current compiler guidance also does not justify removing all
manual memoization without checking the active build and measured behavior.

## Review traps

Look for local state seeded once from changing props; index keys in editable lists; effect
cleanup that removes another instance's listener; inputs switching controlledness; and
successful network calls incorrectly treated as confirmed device outcomes. Write focused
tests that reproduce these, not snapshots of component internals.

## Sources

Use documentation matching the installed version.

- [React effects and derived values](https://react.dev/learn/you-might-not-need-an-effect)
- [Effect lifecycle](https://react.dev/reference/react/useEffect)
- [React Compiler](https://react.dev/learn/react-compiler)
- [Vercel React guidance reviewed](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md)
- [Vercel composition guidance reviewed](https://github.com/vercel-labs/agent-skills/blob/main/skills/composition-patterns/SKILL.md)

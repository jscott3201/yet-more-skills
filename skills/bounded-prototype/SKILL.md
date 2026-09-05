---
name: bounded-prototype
description: Build an explicitly requested experiment to answer one design, integration, performance, or UI question. Keep it isolated and honest; not production delivery, a mandatory HTML demo, or permission to publish.
license: MIT OR Apache-2.0
---

# Bounded Prototype

Choose the smallest runnable experiment that can change a decision. Start with the uncertainty and what observation would support or reject an approach. Avoid building an entire product to answer a narrow question.

## Choose the right evidence

Use the existing stack and an isolated fixture, scratch project, example target, or prototype route. A state-model question may benefit from an interactive demo; a Rust/Python boundary question may need a small release-built benchmark; a durability question may need controlled failure injection. HTML is an option, not a requirement.

Set a scope and resource budget before expanding. Prefer one uncertain boundary and representative inputs. Label mock data, stubbed integrations, unsupported capabilities, and provisional results. Do not make a polished demo imply that a backend or physical action exists.

## Keep the experiment safe

Do not use production data, live devices, credentials, billable services, or destructive operations without the necessary authority. Use task-owned scratch persistence when persistence is the subject; no automatic database setup otherwise. Keep the experiment off the production execution path and preserve unrelated files.

A prototype can omit production polish, but it still needs the checks that make its conclusion credible. Keep boundary validation and safe cleanup. For concurrent or native code, do not waive lifetime or memory-safety requirements because the code is temporary.

## Interpret the result narrowly

Expose the relevant state and make the experiment easy to run using repository conventions. For performance, compare equivalent builds and inputs, include variability, and separate setup from the operation of interest. For UI, distinguish source inspection from rendered/browser evidence. For correctness, test the failure that would falsify the design.

Return the question, experiment, observation, limitations, and recommendation. State what would still be required for production. Keep, remove, or promote the prototype only within the user's scope; do not automatically commit a throwaway branch, publish a demo, or alter a tracker.

A useful negative result is completion when it resolves the uncertainty.

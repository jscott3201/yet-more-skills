---
name: ui-equipment-3d
description: 'Build or review requested equipment visualization in an existing Three.js or React Three Fiber UI: scene identity, telemetry, GPU lifetime, performance, and accessible fallbacks. Not a reason to add 3D or migrate frameworks.'
license: MIT OR Apache-2.0
---

# Equipment 3D and Telemetry Views

Use 3D when it helps explain equipment, topology, or an operating state. A dense table or schematic may be the better primary interface. Inspect the installed renderer, framework, asset pipeline, scene model, and existing design system before changing them.

## Keep scene and domain ownership separate

Use stable domain identifiers to connect scene objects, equipment details, selection, and fault evidence. A mesh name or array position should not silently become an equipment identity. Handle stale, missing, disconnected, and invalid telemetry without depicting normal operation.

Separate physical dimensions and units from visual scale. Make flow direction, valve/fan state, and animation meaning explicit and label illustrative geometry. Do not imply engineering accuracy, a digital-twin calibration, or a confirmed physical action from decorative motion.

Keep interaction state in the appropriate UI owner and high-frequency animation in the renderer's supported update path. In React Three Fiber, avoid React state updates every frame. Do not apply React hooks to a Svelte application; use its actual integration or leave that lane unrun.

## Budget resources and preserve usability

Profile frame time, draw calls, loaded assets, and memory on representative equipment counts and hardware. Reuse geometry/materials or instance objects when that actually helps. Avoid unnecessary per-frame allocations, repeated model loading, and permanent rendering of an otherwise idle scene.

Respect ownership when disposing GPU resources: do not dispose a shared cached asset still used elsewhere. Inspect event handlers, subscriptions, controls, animation loops, and cleanup on unmount or site change. Test repeat mount/unmount, failed assets, and graphics-context loss where supported.

Provide an equivalent semantic DOM path to inspect, select, and act on equipment. Preserve keyboard navigation, focus, reduced motion, readable status, and a usable fallback when graphics are unavailable. Do not make a canvas the only way to acknowledge or investigate a fault.

## Validate the rendered result

Inspect realistic dense and sparse scenes, picking/occlusion, narrow layouts, labels, themes, and uncertain telemetry. Distinguish source review, screenshots, actual interaction tests, and measured performance. State what was not exercised.

Reference: [React Three Fiber performance guidance](https://r3f.docs.pmnd.rs/advanced/pitfalls). Match the installed renderer rather than copying current examples blindly.

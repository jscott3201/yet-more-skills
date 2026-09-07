# Consumer-focused package diagnosis

A package can pass its own tests while failing outside the monorepo. Pick the consumer that exposed the problem and work backward from its import, emitted JavaScript, and declaration resolution.

For a Node consumer, inspect the nearest package type and the actual import/require path. For a browser consumer, inspect the chosen export and emitted dependency graph. For a TypeScript consumer, inspect which declaration file is selected under its compiler options. These are different observations, not substitutes for one another.

Useful failure cases are a missing dist file, a relative import accepted only by the development bundler, a declaration referencing a private workspace path, a required package available only through hoisting, and an export-map change that removes a supported subpath. An import smoke test should exercise a meaningful exported operation, not merely load an empty module.

Do not prescribe the latest Node or TypeScript version to fix every mismatch. State the intended support floor and select the smallest supported correction. Node's native type stripping deliberately does not implement full tsconfig transformation or type checking; its supported syntax and dependency rules are version-sensitive.

Sources, checked September 7, 2026: [TypeScript compiler options by host](https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html), [Node package entry points and exports](https://nodejs.org/api/packages.html), [Node TypeScript execution](https://nodejs.org/api/typescript.html). These sources guide inspection, not an automatic configuration template.

#!/usr/bin/env python3
"""Copy selected Codex skills. Preview by default; never overwrite existing skills."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent
CORE = (
    'rust-workflow', 'rust-api-design', 'rust-nextest',
    'rust-test-design', 'rust-performance', 'rust-review',
)
SETS = {
    'core': CORE,
    'protocol': CORE + ('rust-memory-layout', 'rust-async-concurrency',
                        'rust-protocol-codecs', 'rust-workspace-dependencies'),
    'storage': CORE + ('rust-memory-layout', 'rust-async-concurrency',
                       'rust-storage-durability', 'rust-numerics-simd',
                       'rust-workspace-dependencies'),
}

PYTHON_CORE = (
    'python-workflow', 'python-api-typing', 'python-pytest',
    'python-test-design', 'python-performance', 'python-review',
)
PYTHON = PYTHON_CORE + (
    'python-async-concurrency', 'python-threading-workers',
    'python-packaging-environments', 'python-data-boundaries', 'python-ci-release',
)
PYO3 = (
    'pyo3-ownership-errors', 'pyo3-async-lifecycle', 'pyo3-free-threading',
    'pyo3-buffer-performance', 'pyo3-wheel-release',
)
BINDINGS = ('rust-python-bindings',) + PYO3
SETS.update({
    'python-core': PYTHON_CORE,
    'python': PYTHON,
    'bindings': BINDINGS,
    'python-rust': PYTHON + BINDINGS,
    'python-additions': PYTHON + PYO3,
})

# Additive frontend sets; existing Rust/Python selections keep their behavior.
SETS.update({'typescript-core': ('typescript-workflow', 'typescript-contracts', 'typescript-async-resources', 'vite-build-tooling', 'ui-data-forms', 'ui-accessibility', 'ui-vitest-testing', 'typescript-review'), 'typescript': ('typescript-workflow', 'typescript-contracts', 'typescript-async-resources', 'vite-build-tooling', 'react-components-state', 'react-performance', 'svelte-components-runes', 'sveltekit-boundaries', 'shadcn-react-components', 'shadcn-svelte-components', 'ui-data-forms', 'ui-accessibility', 'ui-design-review', 'ui-operational-workflows', 'ui-graph-editors', 'ui-tables-large-data', 'ui-vitest-testing', 'ui-playwright-validation', 'ui-browser-performance', 'ui-security-boundaries', 'typescript-review', 'ui-ci-release'), 'typescript-additions': ('typescript-workflow', 'typescript-contracts', 'typescript-async-resources', 'vite-build-tooling', 'react-components-state', 'react-performance', 'svelte-components-runes', 'sveltekit-boundaries', 'shadcn-react-components', 'shadcn-svelte-components', 'ui-data-forms', 'ui-accessibility', 'ui-design-review', 'ui-operational-workflows', 'ui-graph-editors', 'ui-tables-large-data', 'ui-vitest-testing', 'ui-playwright-validation', 'ui-browser-performance', 'ui-security-boundaries', 'typescript-review', 'ui-ci-release'), 'react-ui': ('typescript-workflow', 'typescript-contracts', 'typescript-async-resources', 'vite-build-tooling', 'ui-data-forms', 'ui-accessibility', 'ui-vitest-testing', 'typescript-review', 'ui-design-review', 'ui-operational-workflows', 'ui-tables-large-data', 'ui-playwright-validation', 'ui-browser-performance', 'react-components-state', 'react-performance', 'shadcn-react-components'), 'svelte-ui': ('typescript-workflow', 'typescript-contracts', 'typescript-async-resources', 'vite-build-tooling', 'ui-data-forms', 'ui-accessibility', 'ui-vitest-testing', 'typescript-review', 'ui-design-review', 'ui-operational-workflows', 'ui-tables-large-data', 'ui-playwright-validation', 'ui-browser-performance', 'svelte-components-runes', 'sveltekit-boundaries', 'shadcn-svelte-components'), 'ui-review': ('typescript-review', 'ui-accessibility', 'ui-design-review', 'ui-security-boundaries', 'ui-playwright-validation', 'ui-browser-performance')})

SETS["workflow"] = ('behavior-first-implementation', 'bounded-pr-slice', 'cross-platform-agent-instructions', 'design-interview', 'diagnosis-loop', 'domain-language', 'handoff-continuity', 'immutable-pr-review', 'module-design', 'orchestrate', 'owner-decision-gate', 'parallel-portfolio', 'pr-gate-loop', 'repository-grounding', 'source-verification', 'tracer-bullet-planning')

# Focused workflow and system-boundary selections.
SETS.update({
    'workflow-lite': ('repository-grounding', 'source-verification', 'diagnosis-loop', 'bounded-pr-slice', 'handoff-continuity'),
    'skill-review-additions': ('simplify-existing-code', 'bounded-prototype', 'agent-tool-boundaries', 'memory-context-hygiene', 'edge-cloud-sync', 'building-fdd-validation', 'ui-equipment-3d'),
    'agent-systems': ('agent-tool-boundaries', 'memory-context-hygiene'),
    'building-systems': ('edge-cloud-sync', 'building-fdd-validation'),
    'equipment-ui': ('ui-equipment-3d',),
})

# Additive engineering and agent-experience selections.
SETS.update({
    'engineering-additions': ('agent-cli-design', 'typescript-package-boundaries', 'cross-language-contracts', 'ui-agent-collaboration'),
    'agent-experience': ('agent-tool-boundaries', 'memory-context-hygiene', 'agent-cli-design', 'ui-agent-collaboration'),
    'typescript-packages': ('typescript-contracts', 'typescript-package-boundaries'),
    'cross-language': ('rust-api-design', 'python-api-typing', 'typescript-contracts', 'cross-language-contracts'),
})

def describe_skills(selected: list[str], *, search: str | None = None,
                    limit: int | None = None) -> dict[str, object]:
    """Return catalog metadata only; do not inspect or prepare a destination."""
    catalog = json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
    rows = catalog['skills']
    by_name = {row['name']: row for row in rows}
    if len(by_name) != len(rows):
        raise ValueError('Duplicate skill names in catalog.json')
    result = [by_name[name] for name in selected]
    for row in result:
        if not isinstance(row['description'], str) or type(row['implicit']) is not bool:
            raise ValueError(f"Invalid discovery metadata for {row['name']}")
    if search is not None:
        terms = search.casefold().split()
        result = [row for row in result if all(
            term in ' '.join(str(row.get(key, '')) for key in
                             ('name', 'title', 'description', 'group')).casefold()
            for term in terms
        )]
    listing = {'pack': catalog['pack'], 'skills': result}
    if limit is not None:
        listing['total_matches'] = len(result)
        listing['truncated'] = len(result) > limit
        listing['skills'] = result[:limit]
    return listing


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--set', choices=(*SETS, 'full'), default=None,
                        help='Select a set; without --set/--skill, defaults to core.')
    parser.add_argument('--skill', action='append', default=[], metavar='NAME',
                        help='Select a named skill, or add it to --set; repeat as needed.')
    parser.add_argument('--dest', type=Path, default=Path.home()/'.agents'/'skills',
                        help='Destination skills directory (default: ~/.agents/skills).')
    parser.add_argument('--apply', action='store_true', help='Copy files; otherwise only preview.')
    parser.add_argument('--list', action='store_true',
                        help='Read-only skill discovery; lists all skills unless --set/--skill filters it.')
    parser.add_argument('--json', action='store_true',
                        help='Emit one JSON document for --list; diagnostics remain on stderr.')
    parser.add_argument('--search', metavar='TEXT',
                        help='With --list, match all whitespace-separated words in catalog metadata (case-insensitive substrings).')
    parser.add_argument('--limit', type=int, metavar='N',
                        help='With --list, return at most N skills and disclose omitted matches; no limit by default.')
    args = parser.parse_args(argv)
    if (args.search is not None or args.limit is not None) and not args.list:
        parser.error('--search and --limit require --list.')
    if args.search is not None and not args.search.strip():
        parser.error('--search requires non-empty text.')
    if args.limit is not None and args.limit < 1:
        parser.error('--limit must be a positive integer.')
    if args.json and not args.list:
        parser.error('--json requires --list.')
    if args.list and args.apply:
        parser.error('--list cannot be combined with --apply.')
    available = {p.name: p for p in (ROOT/'skills').iterdir()
                 if p.is_dir() and (p/'SKILL.md').is_file()}
    if args.set == 'full' or (args.list and not args.set and not args.skill):
        selected = list(available)
    elif args.set:
        selected = list(SETS[args.set])
    else:
        selected = [] if args.skill else list(CORE)
    selected = sorted(set(selected + args.skill))
    unknown = sorted(set(selected) - set(available))
    if unknown:
        parser.error('Unknown skill(s): ' + ', '.join(unknown))
    if args.list:
        try:
            listing = describe_skills(selected, search=args.search, limit=args.limit)
        except (OSError, ValueError, KeyError, TypeError) as error:
            parser.error(f'Cannot list skills from catalog.json: {error}')
        if args.json:
            print(json.dumps(listing, ensure_ascii=False, indent=2))
        else:
            for row in listing['skills']:
                policy = '' if row['implicit'] else ' [explicit-only]'
                print(f"{row['name']}{policy}\n  {row['description']}")
            if not listing['skills']:
                print('No matching skills in the selected catalog scope.')
            if listing.get('truncated'):
                print(f"Showing {len(listing['skills'])} of {listing['total_matches']} matches; narrow --search or increase --limit.")
        return 0
    dest = args.dest.expanduser().resolve()
    if dest.exists() and not dest.is_dir():
        parser.error(f'Destination is not a directory: {dest}')
    # Preflight the entire selection, including dangling destination symlinks.
    collisions = [name for name in selected
                  if (dest/name).exists() or (dest/name).is_symlink()]
    if collisions:
        parser.error('Existing skills will not be overwritten: ' + ', '.join(collisions)
                     + '. Review them and choose a different selection/destination.')
    for name in selected:
        source = available[name]
        if source.is_symlink() or any(p.is_symlink() for p in source.rglob('*')):
            parser.error(f'Source skill contains a symlink; inspect it before copying: {name}')
        if source == dest or source in dest.parents:
            parser.error('Destination cannot be inside a source skill.')
    for name in selected:
        print(f'{available[name]} -> {dest/name}')
    if not args.apply:
        print(f'Preview only: {len(selected)} skills. Add --apply to copy.')
        return 0
    # copytree also refuses any destination that appears after preflight.
    # An I/O failure can leave a partial new copy; report it without deleting user data.
    try:
        dest.mkdir(parents=True, exist_ok=True)
        for name in selected:
            shutil.copytree(available[name], dest/name,
                            ignore=shutil.ignore_patterns('.DS_Store', '__pycache__', '*.pyc'))
            for license_name in ('LICENSE-MIT', 'LICENSE-APACHE'):
                license_path = ROOT/license_name
                if license_path.is_file():
                    shutil.copy2(license_path, dest/name/license_name)
    except OSError as error:
        print(f'Installation stopped: {error}. Some new copies may be partial; '
              'inspect the destination before retrying.', file=sys.stderr)
        return 1
    print(f'Installed {len(selected)} skills. Existing configurations were not changed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Check catalog/frontmatter/sidecar agreement with real YAML parsing.

Authoring dependency: PyYAML. This does not test host discovery or agent behavior.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    raise SystemExit('PyYAML is required for metadata validation; install it in your authoring environment.')


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'Duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def validate(root: Path) -> int:
    rows = json.loads((root/'catalog.json').read_text())['skills']
    names = [row['name'] for row in rows]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate catalog names')
    if set(names) != {p.parent.name for p in (root/'skills').glob('*/SKILL.md')}:
        raise ValueError('Catalog and skill directories differ')
    for row in rows:
        name = row['name']
        folder = root/'skills'/name
        text = (folder/'SKILL.md').read_text()
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            raise ValueError(f'{name}: missing frontmatter')
        front = yaml.load(text[4:].split('\n---\n', 1)[0], Loader=UniqueLoader)
        sidecar = yaml.load((folder/'agents/openai.yaml').read_text(), Loader=UniqueLoader)
        if front['name'] != name or front['description'] != row['description']:
            raise ValueError(f'{name}: catalog/frontmatter mismatch')
        if sidecar['interface']['display_name'] != row['title']:
            raise ValueError(f'{name}: catalog/display title mismatch')
        implicit = sidecar.get('policy', {}).get('allow_implicit_invocation', True)
        if type(implicit) is not bool or implicit != row['implicit']:
            raise ValueError(f'{name}: invocation policy mismatch')
        if name in ('orchestrate', 'pr-gate-loop') and implicit:
            raise ValueError(f'{name}: must remain explicit-only')
        for license_name in ('LICENSE-MIT', 'LICENSE-APACHE'):
            if (folder/license_name).exists() and (folder/license_name).read_bytes() != (root/license_name).read_bytes():
                raise ValueError(f'{name}: noncanonical {license_name}')
    return len(rows)


if __name__ == '__main__':
    try:
        count = validate(Path(__file__).resolve().parents[1])
    except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
        sys.exit(str(error))
    print(f'Metadata and canonical licenses validated for {count} skills.')

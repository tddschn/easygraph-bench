#!/usr/bin/env python3

from pathlib import Path
import json
from collections import defaultdict

j = Path('semgrep-output.json')
d = json.loads(j.read_text())
r = d['results']
calls = defaultdict(list)

for item in r:
    tool_name = item['path'].removesuffix('_profile.py')
    calls[tool_name].append(item['extra']['lines'])

for k, v in calls.items():
    for i, f in enumerate(v):
        nf = f.removeprefix('benchmark(')
        nf = nf.rstrip(')\'"')
        nf = nf.removesuffix('globals=globals(), n=n')
        v[i] = nf.strip()
    calls[k] = v

methods = [
    'loading',
    'shortest path',
    'page rank',
    'k-core',
    'strongly connected components',
]
methods6 = methods.copy()
methods6.insert(1, '2-hops')
c = {}
for k, v in calls.items():
    c[k] = {}
    num_method = len(v)
    if num_method == 5:
        for i, m in enumerate(methods):
            c[k][m] = v[i]
    else:
        for i, m in enumerate(methods6):
            c[k][m] = v[i]

Path('graph-benchmark-code.json').write_text(json.dumps(c))

#!/usr/bin/env python3

import json
from pathlib import Path
from tomark import Tomark

json_path = Path('./graph_info.json')
graph_info_d = json.loads(json_path.read_text())
data: list[dict[str, str | int | bool]] = []
for graph_name, graph_info in graph_info_d.items():
    data.append({'Dataset Name': graph_name, **graph_info})

markdown = Tomark.table(data)  # type: ignore
print(markdown)

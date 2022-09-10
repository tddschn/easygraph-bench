#!/usr/bin/env python3

import json
from pathlib import Path
from tomark import Tomark
from config import dataset_homepage_mapping

json_path = Path('./graph_info.json')
graph_info_d = json.loads(json_path.read_text())
data: list[dict[str, str | int | bool]] = []
for graph_name, graph_info in graph_info_d.items():
    if graph_name in dataset_homepage_mapping:
        homepage = dataset_homepage_mapping[graph_name]
        data.append({'Dataset Name': f'[{graph_name}]({homepage})', **graph_info})
    else:
        data.append({'Dataset Name': graph_name, **graph_info})

markdown = Tomark.table(data)  # type: ignore
print(markdown)

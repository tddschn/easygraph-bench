#!/usr/bin/env python3

# %%
from config import graph_info_json_path
from utils_other import get_pretty_graph_name

# %%
from pathlib import Path
import json

gi = json.loads(graph_info_json_path.read_text())

# %%
# rename every key in gi to its pretty name
gi = {get_pretty_graph_name(k): v for k, v in gi.items()}
# save gi to graph_info.json
graph_info_json_path.write_text(json.dumps(gi, indent=2))

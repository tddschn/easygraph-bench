import json
from functools import cache
from config import graph_info_json_path


@cache
def get_dataset_list_sorted_by_nodes() -> list[str]:
    gi_d = json.loads(graph_info_json_path.read_text())
    return sorted(gi_d, key=lambda x: gi_d[x]['nodes'])

import json
from functools import cache
from config import graph_info_json_path


@cache
def get_dataset_list_sorted_by_nodes_and_edges() -> list[str]:
    gi_d = json.loads(graph_info_json_path.read_text())
    return sorted(gi_d, key=lambda x: (gi_d[x]['nodes'], gi_d[x]['edges']))


def is_dataset_directed(dataset_name: str) -> bool:
    gi_d = json.loads(graph_info_json_path.read_text())
    return gi_d[dataset_name]['is_directed']

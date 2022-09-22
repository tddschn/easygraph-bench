from pathlib import Path
from itertools import count
import json
from functools import cache
from typing import Iterator
from config import graph_info_json_path


@cache
def get_dataset_list_sorted_by_nodes_and_edges() -> list[str]:
    gi_d = json.loads(graph_info_json_path.read_text())
    return sorted(gi_d, key=lambda x: (gi_d[x]['nodes'], gi_d[x]['edges']))


def is_dataset_directed(dataset_name: str) -> bool:
    gi_d = json.loads(graph_info_json_path.read_text())
    return gi_d[dataset_name]['is_directed']


def autorange_count_generator() -> Iterator[int]:
    base_nums = [1, 2, 5]
    for i in count():
        multiplier = 10**i
        for base_num in base_nums:
            yield base_num * multiplier


def get_autorange_count(average_time: float) -> int:  # type: ignore
    if average_time <= 0:
        raise ValueError('average_time must be positive')
    for cnt in autorange_count_generator():
        if average_time * cnt >= 0.2:
            return cnt

def strip_file_content(filename: Path) -> None:
    content = Path(filename).read_text()
    Path(filename).write_text(content.strip())
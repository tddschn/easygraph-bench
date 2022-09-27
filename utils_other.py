from difflib import SequenceMatcher
from pathlib import Path
from itertools import count
import json
from functools import cache
from typing import Any, Callable, Iterable, Iterator, TypeVar
from config import graph_info_json_path

T = TypeVar('T')


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


def strip_file_content(filename: Path, append: str = '\n') -> None:
    content = Path(filename).read_text()
    Path(filename).write_text(content.strip() + append)


def similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def f7(
    seq: Iterable[T], key: Callable[[T], Any] | None, keep_last: bool = False
) -> Iterable[T]:
    # https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
    seen = set()
    seen_add = seen.add
    if keep_last:
        seq = reversed(seq)  # type: ignore
    if key is None:
        result = iter(x for x in seq if not (x in seen or seen_add(x)))
    else:
        result = iter(x for x in seq if not (key(x) in seen or seen_add(key(x))))
    if keep_last:
        return reversed(list(result))
    return result

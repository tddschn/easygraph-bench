#!/usr/bin/env python3

from hr_tddschn import hr
from easygraph import multi_source_dijkstra, read_edgelist, DiGraph
from utils_other import autorange_count_generator
from itertools import islice
from random import sample
from benchmark import benchmark_autorange


def test_multi_source_dijkstra(edgelist_path: str) -> list[dict[int, float]]:
    amz = read_edgelist(
        edgelist_path, delimiter="\t", nodetype=int, create_using=DiGraph()
    ).cpp()  # type: ignore
    amz_l = []
    nodes = amz.nodes
    num_nodes = len(amz.nodes)
    for num in islice(autorange_count_generator(), 20):
        if num > num_nodes:
            break
        sources = sample(amz.nodes.keys(), num)
        amz_l.append(
            {
                num: benchmark_autorange(
                    'multi_source_dijkstra(amz, sources)', globals=globals() | locals()
                )
            }
        )

    return amz_l


def main() -> None:

    l = []
    for p in [
        'enron.txt',
        'amazon.txt',
        'google.txt',
        'pokec.txt',
    ]:
        print(p)
        result = test_multi_source_dijkstra(p)
        l.append(result)
        print(result)
        hr()

    import json
    from pathlib import Path

    Path('multi_source_dijkstra_test_result.json').write_text(json.dumps(l, indent=2))
    print(f'Wrote to {Path("multi_source_dijkstra_test_result.json").resolve()}')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from hr_tddschn import hr
from easygraph import multi_source_dijkstra, read_edgelist, DiGraph
from utils_other import autorange_count_generator
from itertools import islice
from random import sample
import random
from benchmark import benchmark_autorange


def test_multi_source_dijkstra(
    edgelist_path: str, seed: int = 0
) -> list[dict[int, float]]:
    g = read_edgelist(
        edgelist_path, delimiter="\t", nodetype=int, create_using=DiGraph()
    ).cpp()  # type: ignore
    g_l = []
    nodes = g.nodes
    num_nodes = len(g.nodes)
    for num in islice(autorange_count_generator(), 20):
        if num > num_nodes:
            break

        random.seed(seed)
        sources = sample(g.nodes.keys(), num)
        g_l.append(
            {
                num: benchmark_autorange(
                    'multi_source_dijkstra(amz, sources)', globals=globals() | locals()
                )
            }
        )

    return g_l


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

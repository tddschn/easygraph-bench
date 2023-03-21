#!/usr/bin/env python3

from easygraph import multi_source_dijkstra, read_edgelist
from utils_other import autorange_count_generator
from itertools import islice
from benchmark import benchmark_autorange
    
def test_multi_source_dijkstra(edgelist_path: str) -> list[dict[int, float]]:
    amz = read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.DiGraph()).cpp()
    amz_l = []
    nodes = amz.nodes
    num_nodes = len(amz.nodes)
    for num in islice(autorange_count_generator(), 20):
        if num > num_nodes:
            break
        sources = sample(amz.nodes.keys(), num)
        amz_l.append({num: benchmark_autorange('multi_source_dijkstra(amz, sources)', globals=globals())})
        
    return amz_l


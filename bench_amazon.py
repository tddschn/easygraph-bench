#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-03
Purpose: EasyGraph & NetworkX side-by-side benchmarking
"""

from hr_tddschn import hr
from pathlib import Path

from config import (
    eg_master_dir,
    load_functions_name,
    di_load_functions_name,
    clustering_methods,
    shortest_path_methods,
    # connected_components_methods,
    connected_components_methods_G,
    connected_components_methods_G_node,
    mst_methods,
    other_methods,
    new_methods,
    method_groups,
    dataset_names,
    BENCH_CSV_DIR,
)
from utils import eg2nx, eg2ceg, nx2eg, get_first_node, eval_method, json2csv, tabulate_csv

# if eg_master_dir.exists():
#     import sys

#     sys.path.insert(0, str(eg_master_dir))

import easygraph as eg
import networkx as nx
from dataset_loaders import load_amazon

load_func_name = 'load_amazon'
if hasattr(load_amazon, 'load_func_for') and load_amazon.load_func_for == 'nx':
    G_nx = load_amazon()
    G_eg = nx2eg(G_nx)
else:
    G_eg = load_amazon()
    G_nx = eg2nx(G_eg)
G_ceg = eg2ceg(G_eg)
first_node_eg = get_first_node(G_eg)
first_node_nx = get_first_node(G_nx)
first_node_ceg = get_first_node(G_ceg)

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='EasyGraph & NetworkX side-by-side benchmarking',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # parser.add_argument(
    #     '-d',
    #     '--dataset',
    #     type=str,
    #     choices=dataset_names,
    #     nargs='+',
    # )

    parser.add_argument(
        '-G', '--method-group', type=str, choices=method_groups, nargs='+'
    )

    parser.add_argument(
        '-C',
        '--skip-cpp-easygraph',
        '--skip-ceg',
        action='store_true',
        help='Skip benchmarking cpp_easygraph methods',
    )

    # parser.add_argument('-n', '--dry-run', action='store_true', help='Dry run')

    parser.add_argument(
        '-D', '--skip-draw', action='store_true', help='Skip drawing graphs to speed things up'
    )

    parser.add_argument(
        '-p', '--pass', type=int, help='Number of passes to run in the benchmark, uses Timer.autorange() if not set.'
    )

    # parser.add_argument(
    #     '-t', '--timeout', type=int, help='Timeout for benchmarking one method in seconds, 0 for no timeout', default=60
    # )
    parser.add_argument(
        '-o', '--output-dir', type=Path, help='Output directory', default=BENCH_CSV_DIR,
    )

    parser.add_argument(
        '-a', '--append-results', action='store_true', help='Append results to existing csv files. Overwrites by default.'
    )

    parser.add_argument(
        '--graph-type', type=str, choices=['directed', 'undirected', 'all'], help='Only run bench if graph is of specified graph type', default='all',
    )

    return parser.parse_args()




def main():
    args = get_args()
    method_groups = args.method_group
    flags = {}
    flags |= {'skip_ceg': args.skip_cpp_easygraph}
    flags |= {'skip_draw': args.skip_draw}
    flags |= {'timeit_number': getattr(args, 'pass', None)}
    # flags |= {'timeout': args.timeout if args.timeout > 0 else None}
    result_dicts: list[dict] = []
    first_node_args = {
        'call_method_args_eg': ['first_node_eg'],
        'call_method_args_nx': ['first_node_nx'],
        'call_method_args_ceg': ['first_node_ceg'],
    }
    if method_groups is None or 'clustering' in method_groups:
        # bench: clustering
        for method_name in clustering_methods:
            _ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)

    if method_groups is None or 'shortest-path' in method_groups:
        # bench: shortest path
        # bench_shortest_path(cost_dict, g, load_func_name)
        _ = eval_method(
            load_func_name,
            ('Dijkstra', 'single_source_dijkstra_path'),
            **first_node_args,
            **flags,
        )
        result_dicts.append(_)
    if method_groups is None or 'connected-components' in method_groups:
        # bench: connected components
        for method_name in connected_components_methods_G:
            _ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)
        for method_name in connected_components_methods_G_node:
            _ = eval_method(
                load_func_name,
                method_name,
                **first_node_args,
                **flags,
            )
            result_dicts.append(_)
    if method_groups is None or 'mst' in method_groups:
        # bench: mst
        for method_name in mst_methods:
            _ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)

    if method_groups is None or 'other' in method_groups:
        # bench: other
        for method_name in other_methods:
            _ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)

    if method_groups is None or 'new' in method_groups:
        # bench: other
        for method_name in new_methods:
            _ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)

    print()
    from mergedeep import merge
    
    result = merge(*result_dicts)
    

    csv_file = f'{load_func_name.removeprefix("load_")}.csv'
    csv_file_path = args.output_dir / csv_file
    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_file_path_s = str(csv_file_path)
    json2csv(result, csv_file_path_s, append=args.append_results)
    print(f'Result saved to {csv_file_path_s} .')
    
    # print csv_file with tabulate
    
    
    print(tabulate_csv(csv_file_path_s))




if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-03
Purpose: EasyGraph & NetworkX side-by-side benchmarking
"""

from hr_tddschn import hr
from pathlib import Path
from tempfile import mkstemp
import sqlite3
from utils_db import insert_bench_results

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
    tool_name_mapping_for_DTForTools,
    bench_results_db_path,
    tool_name_mapping,
)
from utils import eg2nx, eg2ceg, nx2eg, get_first_node, eval_method, json2csv, tabulate_csv
from eg_bench_types import DTForTools

# if eg_master_dir.exists():
#     import sys

#     sys.path.insert(0, str(eg_master_dir))

import easygraph as eg
import networkx as nx
from dataset_loaders import load_pgp

load_func_name = 'load_pgp'
if hasattr(load_pgp, 'load_func_for') and load_pgp.load_func_for == 'nx':  # type: ignore
    G_nx = load_pgp()
    G_eg = nx2eg(G_nx)  # type: ignore
else:
    G_eg = load_pgp()
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
        '-E', '--skip-easygraph', action='store_true', help='Skip benchmarking easygraph (python) method',
    )

    parser.add_argument(
        '-C',
        '--skip-cpp-easygraph',
        '--skip-ceg',
        action='store_true',
        help='Skip benchmarking cpp_easygraph methods',
    )

    parser.add_argument(
        '-N', '--skip-networkx', action='store_true', help='Skip benchmarking networkx method',
    )

    # parser.add_argument('-n', '--dry-run', action='store_true', help='Dry run')

    

    parser.add_argument(
        '-p', '--pass', type=int, help='Number of passes to run in the benchmark, uses Timer.autorange() if not set.'
    )

    # parser.add_argument(
    #     '-t', '--timeout', type=int, help='Timeout for benchmarking one method in seconds, 0 for no timeout', default=60
    # )

    # parser.add_argument(
    #     '--paper', action='store_true', help='Use this flag to generate the results for the paper'
    # )

    parser.add_argument(
        '-o', '--output-dir', type=Path, help='Output directory', default=BENCH_CSV_DIR,
    )

    parser.add_argument(
        '-a', '--append-results', action='store_true', help='Append results to existing csv files. Overwrites by default.'
    )

    parser.add_argument(
        '-S', '--no-save', action='store_true', help='Do not save results to csv files or the database.'
    )

    parser.add_argument(
        '--graph-type', type=str, choices=['directed', 'undirected', 'all'], help='Only run bench if graph is of specified graph type', default='all',
    )

    parser.add_argument(
        '--db-path',
        metavar='PATH',
        type=Path,
        help='Path to the sqlite3 database',
        default=bench_results_db_path,
    )

    parser.add_argument(
        '--no-update-db', action='store_true', help='Do not update the sqlite3 database with the new results.'
    )

    return parser.parse_args()




def main():
    args = get_args()
    method_groups = args.method_group
    flags = {}
    flags |= {'skip_eg': args.skip_easygraph}
    flags |= {'skip_ceg': args.skip_cpp_easygraph}
    flags |= {'skip_networkx': args.skip_networkx}
    flags |= {'skip_draw': True}
    flags |= {'timeit_number': getattr(args, 'pass', None)}
    # flags |= {'timeout': args.timeout if args.timeout > 0 else None}
    result_dicts: list[dict] = []
    bench_timestamps: list[DTForTools] = []
    first_node_args = {
        'call_method_args_eg': ['first_node_eg'],
        'call_method_args_nx': ['first_node_nx'],
        'call_method_args_ceg': ['first_node_ceg'],
    }
    if method_groups is None or 'clustering' in method_groups:
        # bench: clustering
        for method_name in clustering_methods:
            _, __ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)
            bench_timestamps.append(__)

    if method_groups is None or 'shortest-path' in method_groups:
        # bench: shortest path
        # bench_shortest_path(cost_dict, g, load_func_name)
        _, __ = eval_method(
            load_func_name,
            ('Dijkstra', 'single_source_dijkstra_path'),
            **first_node_args,
            **flags,
        )
        result_dicts.append(_)
        bench_timestamps.append(__)
    if method_groups is None or 'connected-components' in method_groups:
        # bench: connected components
        for method_name in connected_components_methods_G:
            _, __ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)
            bench_timestamps.append(__)
        for method_name in connected_components_methods_G_node:
            _, __ = eval_method(
                load_func_name,
                method_name,
                **first_node_args,
                **flags,
            )
            result_dicts.append(_)
            bench_timestamps.append(__)
    if method_groups is None or 'mst' in method_groups:
        # bench: mst
        for method_name in mst_methods:
            _, __ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)
            bench_timestamps.append(__)

    if method_groups is None or 'other' in method_groups:
        # bench: other
        for method_name in other_methods:
            _, __ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)
            bench_timestamps.append(__)


    if method_groups is None or 'new' in method_groups:
        # bench: other
        for method_name in new_methods:
            _, __ = eval_method(
                load_func_name,
                method_name,
                **flags,
            )
            result_dicts.append(_)
            bench_timestamps.append(__)


    print()
    from mergedeep import merge
    
    result = merge(*result_dicts)
    # print(f'{result_dicts=}')
    # print(f'{result=}')

    dataset_name = load_func_name.removeprefix("load_")
    csv_file = f'{dataset_name}.csv'
    csv_file_path = args.output_dir / csv_file
    if args.no_save:
        _, csv_file_path_s = mkstemp(suffix='.csv')
        csv_file_path = Path(csv_file_path_s)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_file_path_s = str(csv_file_path)
    json2csv(result, csv_file_path_s, append=args.append_results)
    print(f'Result saved to {csv_file_path_s} .')
    # print csv_file with tabulate
    print(tabulate_csv(csv_file_path_s))
    if args.no_save:
        csv_file_path.unlink()
        print(f'Removed temporary csv file at {csv_file_path_s} .')
    
    if args.no_update_db:
        return

    with sqlite3.connect(args.db_path) as conn:
        print(f'Writing new results to database at {args.db_path} .')
        for i, (dataset_name, data) in enumerate(result.items()):
            dt_for_tools = bench_timestamps[i]
            # result is like
            # {'stub': {'average_clustering': {'easygraph': 0.00047430999984499067,
            #                                  'eg w/ C++ binding': 7.46910081943497e-05,
            #                                  'networkx': 0.00028450800164137036},
            #           'clustering': {'easygraph': 0.00010412100527901202,
            #                          'eg w/ C++ binding': 4.4621992856264114e-05,
            #                          'networkx': 0.00013218499952927232}}}
            for method, tool_time_mapping in data.items():
                for tool, avg_time in tool_time_mapping.items():
                    insert_bench_results(
                        conn,
                        dataset=dataset_name,
                        method=method,
                        tool=tool_name_mapping[tool] if tool in tool_name_mapping else tool,
                        average_time=avg_time,
                        timestamp=getattr(dt_for_tools, tool_name_mapping_for_DTForTools[tool]),
                        iteration_count=getattr(args, 'pass', None),
                    )
    print(f'Finished writing new results to database at {args.db_path} .')





if __name__ == "__main__":
    main()
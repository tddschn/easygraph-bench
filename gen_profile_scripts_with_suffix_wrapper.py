#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-03-23
Purpose: wrapper around gen_bench_script.py's --profile-suffix workflow
"""

import argparse
from copy import deepcopy
from pathlib import Path
from config import graph_benchmark_method_order, edgelist_filenames, edgelist_filenames_lcc


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='wrapper around gen_bench_script.py\'s --profile-suffix workflow',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'suffix',
        # dest='profile_suffix',
        help='suffix for profile scripts (--profile-suffix)',
        type=str,
        default='',
    )

    parser.add_argument(
        '-t',
        '--tools',
        dest='profile_select_tools',
        help='select tools for profiling, (--profile-select-tools)',
        type=str,
        nargs='+',
        choices=['igraph', 'graphtool', 'networkit', 'easygraph', 'networkx', 'snap'],
        default=['igraph', 'graphtool', 'networkit', 'easygraph', 'networkx', 'snap'],
    )

    parser.add_argument(
        '-m',
        '--methods',
        dest='profile_select_methods',
        help='select methods for profiling (--profile-select-methods)',
        type=str,
        nargs='+',
        choices=graph_benchmark_method_order,
        default=graph_benchmark_method_order,
    )

    parser.add_argument(
        '-d',
        '--datasets',
        dest='profile_select_datasets',
        help='select datasets for profiling (--profile-select-datasets)',
        type=str,
        nargs='+',
        choices=edgelist_filenames + edgelist_filenames_lcc,
        default=edgelist_filenames + edgelist_filenames_lcc,
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    args.profile_suffix = args.suffix
    del args.suffix  # type: ignore
    args_profile = deepcopy(args)
    args_profile_entrypoint = deepcopy(args)
    args_profile.profile = True
    args_profile_entrypoint.profile_entrypoint = True
    # from icecream import ic

    # ic(args_profile)
    # ic(args_profile_entrypoint)
    from gen_bench_script import main as gen_bench_script_main

    gen_bench_script_main(args_profile)
    gen_bench_script_main(args_profile_entrypoint)


if __name__ == '__main__':
    main()

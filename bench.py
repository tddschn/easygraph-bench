#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-03
Purpose: EasyGraph & NetworkX side-by-side benchmarking
"""

from sys import argv
from config import method_groups, known_individual_bench_scripts

import argparse
from subprocess import run


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='EasyGraph & NetworkX side-by-side benchmarking (Runs on all datasets by invoking `./bench_*.py`)',
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

    return parser.parse_args()


args = get_args()


def main():
    # print(f'{args=}')
    # print(f'{argv=}')
    for script in known_individual_bench_scripts:
        print(f'Running {script}')
        run([f'./{script}', *argv[1:]])


if __name__ == "__main__":
    main()

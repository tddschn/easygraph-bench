#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-03
Purpose: EasyGraph & NetworkX side-by-side benchmarking

Why do you repeat yourself by using `bench_*.py` scripts?

Yeah, I know this is not dry. But for the timeit-based benchmarking code to work,
`eg`, `nx` and the graph objects must be in the global scope, i.e. `__main__`. 

I don't know how to do that while sticking to the DRY principle. 

But if you know, please tell me. :)
"""

from sys import argv
from config import method_groups, {{ script_set_list }}

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

    parser.add_argument(
        '-D',
        '--skip-draw',
        action='store_true',
        help='Skip drawing graphs to speed things up',
    )

    parser.add_argument(
        '-p',
        '--pass',
        metavar='NUMBER',
        type=int,
        help='Number of passes to run in the benchmark, uses Timer.autorange() if not set.',
    )

    parser.add_argument(
        '-t', '--timeout', type=int, help='Timeout for benchmarking one method in seconds, 0 for no timeout', default=60
    )

    parser.add_argument(
        '-a', '--append-results', action='store_true', help='Append results to existing csv files. Overwrites by default.'
    )


    return parser.parse_args()


args = get_args()


def main():
    # print(f'{args=}')
    # print(f'{argv=}')
    number_scripts = len({{ script_set_list }})
    for n, script in enumerate({{ script_set_list }}):
        print(f'Running {script} ({n+1}/{number_scripts})')
        run([f'./{script}', *argv[1:]], check=True)
        print(f'Finished running {script} ({n+1}/{number_scripts})')


if __name__ == "__main__":
    main()

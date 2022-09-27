#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-27
Purpose: Dedupe csv entries
"""

import argparse
from pathlib import Path
from config import BENCH_CSV_DIR
from utils_other import f7


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Dedupe csv entries',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-c',
        '--csv-dir',
        help='Path to the bench result csv dir',
        type=Path,
        default=BENCH_CSV_DIR,
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    csv_dir = args.csv_dir
    for p in csv_dir.glob('*.csv'):
        lines = p.read_text().splitlines()
        lines = f7(lines, key=lambda x: tuple(x.split(',')[:2]), keep_last=True)
        p.write_text('\n'.join(lines))


if __name__ == '__main__':
    main()

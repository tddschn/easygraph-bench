#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-25
Purpose: Create sqlite3 db and tables
"""

import argparse
from pathlib import Path
import sqlite3
from utils_db import init_db
from config import bench_results_db_path


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create sqlite3 db and tables',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '--db-path',
        metavar='PATH',
        type=Path,
        help='Path to the database',
        default=bench_results_db_path,
    )

    parser.add_argument(
        '-f',
        '--force',
        help='Force overwrite existing db',
        action='store_true',
    )

    return parser.parse_args()


def main() -> None:
    args = get_args()
    if args.force:
        args.db_path.unlink(missing_ok=True)
    with sqlite3.connect(args.db_path) as conn:
        init_db(conn)


if __name__ == '__main__':
    main()

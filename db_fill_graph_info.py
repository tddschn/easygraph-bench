#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-25
Purpose: Fill graph info to the sqlite3 db
"""

import argparse
from pathlib import Path
from utils_db import insert_graph_info
from config import bench_results_db_path, graph_info_json_path
import sqlite3, json


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Fill graph info to the sqlite3 db',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '--db-path',
        metavar='PATH',
        type=Path,
        help='Path to the database',
        default=bench_results_db_path,
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    db_path = args.db_path
    with sqlite3.connect(db_path) as conn:
        gi_d = json.loads(graph_info_json_path.read_text())
        insert_graph_info(conn, gi_d)


if __name__ == '__main__':
    main()

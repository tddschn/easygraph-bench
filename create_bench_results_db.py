#!/usr/bin/env python3

from datetime import datetime
from config import (
    bench_results_db_path,
    bench_results_table_name,
    graph_info_table_name,
    graph_info_json_path,
)
import sqlite3, json

python_type_to_sqlite_type = {
    int: 'INTEGER',
    float: 'REAL',
    str: 'TEXT',
    bool: 'INTEGER',
    datetime: 'TEXT',
}


def get_graph_info_field_types() -> dict[str, str]:
    gi_d = json.loads(graph_info_json_path.read_text())
    _, properties = gi_d.popitem()
    graph_property_types = {'dataset': str, 'homepage': str}
    graph_property_types |= {
        property_name: type(value) for property_name, value in properties.items()
    }
    return {
        property_name: python_type_to_sqlite_type[property_type]
        for property_name, property_type in graph_property_types.items()
    }


def get_bench_results_field_types() -> dict[str, str]:
    return {
        'dataset': 'TEXT',
        'method': 'TEXT',
        'tool': 'TEXT',
        'avg time': 'TEXT',
        'iteration count': 'TEXT',
        'datetime': 'TEXT',
    }


def init_db(conn: sqlite3.Connection):
    conn.set_trace_callback(print)
    cursor = conn.cursor()
    #     """CREATE TABLE IF NOT EXISTS "bench-results"(
    # "dataset" TEXT PRIMARY KEY NOT NULL, "method" TEXT, "tool" TEXT, "avg time" TEXT,
    #  "iteration count" TEXT);
    #     """
    graph_info_field_str = ', '.join(
        f'"{field_name}" {field_type}{"" if field_name != "dataset" else " PRIMARY KEY NOT NULL"}'
        for field_name, field_type in get_graph_info_field_types().items()
    )
    bench_results_field_str = ', '.join(
        f'"{field_name}" {field_type}{"" if field_name != "dataset" else " PRIMARY KEY"} NOT NULL'
        for field_name, field_type in get_bench_results_field_types().items()
    )
    graph_info_table_creation_sql = (
        f'CREATE TABLE IF NOT EXISTS "{graph_info_table_name}"({graph_info_field_str});'
    )
    bench_results_table_creation_sql = f'CREATE TABLE IF NOT EXISTS "{bench_results_table_name}"({bench_results_field_str});'
    cursor.execute(graph_info_table_creation_sql)
    cursor.execute(bench_results_table_creation_sql)


def main() -> None:
    with sqlite3.connect(bench_results_db_path) as conn:
        init_db(conn)


if __name__ == '__main__':
    main()

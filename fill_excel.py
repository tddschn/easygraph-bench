#!/usr/bin/env python3


import openpyxl
from openpyxl.cell.cell import Cell, MergedCell
from openpyxl.worksheet.worksheet import Worksheet
from pathlib import Path
from config import tool_name_mapping
import sqlite3


bench_results_sqlite_db_path = Path(__file__).parent / 'bench-results.db'
template_workbook_path = (
    '/Users/tscp/Downloads/easygraph-benchmark-results-template.xlsx'
)
new_workbook_path = '/Users/tscp/Downloads/easygraph-benchmark-results.xlsx'

dataset_name_col = 'A'
tool_col = 'A'
# cSpell:disable
avg_time_cols = list('BCDEF')
# cSpell:enable


def get_dataset_name_to_row_number_mapping(worksheet: Worksheet) -> dict[str, int]:
    rd = worksheet.row_dimensions
    max_row = len(rd)
    row_range = range(1, max_row + 1, 5)
    dataset_name_to_row_number_mapping: dict[str, int] = {
        worksheet[f'{dataset_name_col}{str(row_number)}'].value: row_number
        for row_number in row_range
    }
    return dataset_name_to_row_number_mapping


def query_avg_time(
    cursor: sqlite3.Cursor, database_name: str, tool_abbr: str, method: str
) -> float:
    query = """
    select "avg time" from "bench-results" where "dataset" = :dataset and "tool" = :tool_abbr and "method" = :method
    """
    cursor.execute(
        query, {'dataset': database_name, 'tool_abbr': tool_abbr, 'method': method}
    )
    try:
        return float(cursor.fetchone()[0])
    except:
        return -100.0


def main() -> None:
    workbook = openpyxl.load_workbook(template_workbook_path)
    worksheet = workbook.active
    dataset_name_to_row_number_mapping = get_dataset_name_to_row_number_mapping(
        worksheet=worksheet
    )
    with sqlite3.connect(bench_results_sqlite_db_path) as conn:
        cursor = conn.cursor()
        for dataset_name, row_number in dataset_name_to_row_number_mapping.items():
            for rn in range(row_number + 1, row_number + 4):
                for cn in avg_time_cols:
                    cell = worksheet[f'{cn}{str(rn)}']
                    if isinstance(cell, MergedCell) or cell.value == 'N/A':
                        print(f'skipped cell {cell}')
                        continue
                    tool = worksheet[f'{tool_col}{str(rn)}'].value
                    tool_abbr = tool_name_mapping[tool]
                    method = worksheet[f'{cn}{str(row_number)}'].value
                    cell.value = query_avg_time(cursor, dataset_name, tool_abbr, method)
    workbook.save(new_workbook_path)


if __name__ == '__main__':
    main()

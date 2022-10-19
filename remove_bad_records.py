#!/usr/bin/env python3

# %%
import json
import sqlite3
from config import *

conn = sqlite3.connect(bench_results_db_path)
conn.set_trace_callback(print)
cursor = conn.cursor()

# %%
conn.commit()
conn.close()


# %%

# delete from table "bench_results" where "tool" contains "profile"
cursor.execute(f'DELETE FROM {bench_results_table_name} WHERE tool LIKE "%profile%"')


# %%

# removesuffix "_undirected" from "tool" column
cursor.execute(
    f'UPDATE {bench_results_table_name} SET tool = REPLACE(tool, "_undirected", "")'
)

# %%

# replace "loading_undirected" with "loading" from "method" column
cursor.execute(
    f'UPDATE {bench_results_table_name} SET method = REPLACE(method, "loading_undirected", "loading")'
)

# %%

# gbc = json.loads(graph_benchmark_code_json_path.read_text())
# gbc_methods =
# just use methods6_timlrx


# select all columns except "id" from "bench_results" where "method" in methods6_timlrx
# ordered by "dataset" and "method" and "tool"
# and export to a csv file
cursor.execute(
    f'''SELECT dataset, method, tool, average_time, iteration_count, timestamp FROM {bench_results_table_name} WHERE method IN ({", ".join(f'"{x}"' for x in methods6_timlrx)}) ORDER BY dataset, method, tool'''
)

rows = cursor.fetchall()
print(len(rows))
with open('profile_results.csv', 'w') as f:
    f.write(','.join([d[0] for d in cursor.description]))
    f.write('\n')
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')

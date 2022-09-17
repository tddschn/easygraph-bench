#!/usr/bin/env bash

find output -name 'all*.csv' -delete
python3 ./merge_bench_csv.py -c output >merged.csv
python3 add_graph_info_and_order_tool_to_csv.py merged.csv -A >all.csv
python3 add_graph_info_and_order_tool_to_csv.py merged.csv >all-with-graph-info.csv
python3 add_graph_info_and_order_tool_to_csv.py merged.csv -A -a >all-abbr.csv
python3 add_graph_info_and_order_tool_to_csv.py merged.csv -a >all-abbr-with-graph-info.csv

mv ./all*.csv output -v

REPO='tddschn/easygraph-bench'
TAG='local'
DATE_STR="$(date +"%Y-%m-%dT%H:%M:%S:%z")"
CSV_ZIP_FILENAME="bench-results-csv-${DATE_STR}.zip"

zip -r "${CSV_ZIP_FILENAME}" output

set +e
# don't exit on error
gh release -R "${REPO}" create "${TAG}" --notes "Release from GitHub Actions"
set -e

gh release -R "${REPO}" upload "${TAG}" "${CSV_ZIP_FILENAME}"

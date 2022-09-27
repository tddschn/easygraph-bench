#!/usr/bin/env bash

ADD_GRAPH_INFO_SCRIPT_COMMON_FLAGS="--autorange-iteration-count"

find output -name 'all*.csv' -delete
python3 ./uniqify_csv_entries.py -c output
python3 ./merge_bench_csv.py --remove-records-with-negative-avg-time -c output >merged.csv
eval python3 add_graph_info_and_order_tool_to_csv.py merged.csv "${ADD_GRAPH_INFO_SCRIPT_COMMON_FLAGS}" -A >all.csv
eval python3 add_graph_info_and_order_tool_to_csv.py merged.csv "${ADD_GRAPH_INFO_SCRIPT_COMMON_FLAGS}" >all-with-graph-info.csv
eval python3 add_graph_info_and_order_tool_to_csv.py merged.csv "${ADD_GRAPH_INFO_SCRIPT_COMMON_FLAGS}" -A -a >all-abbr.csv
eval python3 add_graph_info_and_order_tool_to_csv.py merged.csv "${ADD_GRAPH_INFO_SCRIPT_COMMON_FLAGS}" -a >all-abbr-with-graph-info.csv

cp ./all*.csv output -v

# [[ -f bench-results.db ]] && rm -v bench-results.db
# sqlite3 bench-results.db '.import all.csv bench-results --csv'

python3 ./fill_excel.py
cp '/Users/tscp/Downloads/easygraph-benchmark-results.xlsx' output -v
cp '/Users/tscp/Downloads/easygraph-benchmark-results-template.xlsx' output -v

REPO='tddschn/easygraph-bench'
TAG='local'
DATE_STR="$(date +"%Y-%m-%dT%H:%M:%S:%z")"
CSV_ZIP_FILENAME="$(echo "bench-results-csv-${DATE_STR}.zip" | tr ':' '-')"

zip -r "${CSV_ZIP_FILENAME}" output

set +e
# don't exit on error
gh release -R "${REPO}" delete "${TAG}" --yes
# gh release -R "${REPO}" create "${TAG}" --notes "Released from GitHub Actions"
gh release -R "${REPO}" create "${TAG}" --notes-file ./release-note-local

set -e

gh release -R "${REPO}" upload "${TAG}" "${CSV_ZIP_FILENAME}"

echo "https://github.com/tddschn/easygraph-bench/releases/tag/${TAG}"

# file-to-clipboard() {
#     osascript \
#         -e 'on run args' \
#         -e 'set the clipboard to POSIX file (first item of args)' \
#         -e end \
#         "$@"
# }

echo "https://github.com/tddschn/easygraph-bench/releases/download/${TAG}/${CSV_ZIP_FILENAME}" | tee /dev/tty | pbcopy

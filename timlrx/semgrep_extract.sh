#!/usr/bin/env bash

git clone https://github.com/timlrx/graph-benchmarks && cd graph-benchmarks/code || exit
semgrep -c semgrep-benchmark-rules.yaml . --json >benchmark-output.json

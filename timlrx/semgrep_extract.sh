#!/usr/bin/env bash

semgrep -c semgrep-benchmark-rules.yaml . --json >benchmark-output.json

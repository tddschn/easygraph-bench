#!/usr/bin/env bash

python3.10 -m venv venv
source venv/bin/activate
pip install python-easygraph tensorflow

python3 -c 'import easygraph as eg; eg.complete_graph(5).cpp()'

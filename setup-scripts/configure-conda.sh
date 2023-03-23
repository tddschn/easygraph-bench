#!/usr/bin/env bash

conda config --add channels conda-forge
conda config --remove channels forge
pip install pybind11 better-exceptions
pip install pebble hr_tddschn tensorflow torch
mamba install -y networkx graph-tool python-igraph networkit
mamba install -y pyinstrument ipython

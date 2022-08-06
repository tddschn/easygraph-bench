#!/usr/bin/env python3
# """
# Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
# Date   : 2022-08-03
# Purpose: EasyGraph & NetworkX side-by-side benchmarking
# """

# from hr_tddschn import hr

from timeit import Timer
from config import (
    eg_master_dir,
    load_functions_name,
    di_load_functions_name,
    clustering_methods,
    shortest_path_methods,
    # connected_components_methods,
    connected_components_methods_G,
    connected_components_methods_G_node,
    mst_methods,
    method_groups,
    dataset_names,
)
from utils import eg2nx, eg2ceg, get_Timer_args, get_first_node, eval_method

if eg_master_dir.exists():
    import sys

    sys.path.insert(0, str(eg_master_dir))

import easygraph as eg
from dataset_loaders import load_bio, load_cheminformatics, load_eco, load_soc  # type: ignore

load_func_name = 'load_cheminformatics'
G_eg = load_cheminformatics()
# G_nx = eg2nx(G_eg)
G_ceg = eg2ceg(G_eg)
# first_node_eg = get_first_node(G_eg)
# first_node_nx = get_first_node(G_nx)
first_node_ceg = get_first_node(G_ceg)


def main():
    timer_setup = f'from __main__ import eg, G_eg, G_ceg, first_node_ceg'
    t = Timer('eg.Dijkstra(G_ceg, first_node_ceg)', timer_setup)
    res = t.autorange()
    print(res)


if __name__ == "__main__":
    main()

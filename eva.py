#!/usr/bin/env python3

import sys

from config import (
    eg_master_dir,
    load_functions_name,
    di_load_functions_name,
    clustering_methods,
    shortest_path_methods,
)

sys.path.insert(0, str(eg_master_dir))

from dataset_loaders import *
from utils import eval_method


if __name__ == "__main__":

    # 遍历数据集
    for load_func_name in load_functions_name:
        cost_dict = dict()
        print(f'loading dataset with {load_func_name} ...')
        g = eval(load_func_name)()
        # 遍历方法
        for method_name in clustering_methods:
            eval_method(cost_dict, g, load_func_name, method_name)

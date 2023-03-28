#!/usr/bin/env python3


# %%
import pandas as pd
from config import graph_info_json_path

gi = pd.read_json(graph_info_json_path)

# swap the col and row of gi
gi = gi.T

# %%
# remove index that startswith 'stub'
gi = gi[~gi.index.str.startswith('stub')]

# %%
# sort by density, then nodes, from more to fewer
gi = gi.sort_values(by=['density', 'nodes'], ascending=[False, False])

# %%
# gi.info()

# %%
# convert cols in gi that looks like numerical values to integer or float types
# first determine which cols should be integer types, but are of 'object' type
int_cols = ['nodes', 'edges']
bool_cols = ['is_directed']
float_cols = ['average_degree', 'density']
gi[int_cols] = gi[int_cols].astype(int)
gi[bool_cols] = gi[bool_cols].astype(bool)
gi[float_cols] = gi[float_cols].astype(float)


# %%
gi.info()

# %%
def get_pretty_graph_name(graph_name: str) -> str:
    return graph_name.rsplit('/', maxsplit=1)[-1].split('.', maxsplit=1)[0]


# apply this function to create a col of pretty graph names
gi['pretty_graph_name'] = gi.index.map(get_pretty_graph_name)
# set the new col as index, then remove the col
gi = gi.set_index('pretty_graph_name')
# remove type col
gi = gi.drop(columns=['type'])
# gi

# %%
# save gi to file
# use hdf5
gi.to_hdf('graph_info.h5', key='graph_info', mode='w')

import os

print(f'graph_info.h5 saved to {os.getcwd()}')

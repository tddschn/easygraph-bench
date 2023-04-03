#!/usr/bin/env python3

from pathlib import Path


def get_dataset_name(s: str) -> str:
    # remove s's file extension if any
    # s = Path(s).stem
    from utils_other import get_pretty_graph_name

    s = get_pretty_graph_name(s)

    # remove '_lcc' or '_sampled'
    return s.removesuffix('_lcc').removesuffix('_sampled')


def main() -> None:

    import pandas as pd

    # read the DataFrame from the HDF5 file
    with pd.HDFStore('graph_info.h5', mode='r') as store:
        gi = store.get('graph_info')

    # show dupe rows in gi
    gi[gi.duplicated(keep=False)]

    # get the index for duplicated

    gi_dupe_set = set(gi[gi.duplicated(keep=False)].index.tolist())

    # apply this func to di_dupe_set
    gi_dupe_set_to_keep = {get_dataset_name(s) for s in gi_dupe_set}

    gi_dupe_set_to_drop = gi_dupe_set - gi_dupe_set_to_keep

    # save to duplicated_graphs_to_drop.json
    import json

    with open('duplicated_graphs_to_drop.json', 'w') as f:
        json.dump(list(gi_dupe_set_to_drop), f, indent=2)

    print(
        f'saved to duplicated_graphs_to_drop.json: {len(gi_dupe_set_to_drop)} graphs to drop'
    )


if __name__ == '__main__':
    main()

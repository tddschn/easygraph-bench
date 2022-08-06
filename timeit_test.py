#!/usr/bin/env python3

from config import eg_master_dir

if eg_master_dir.exists():
    import sys

    sys.path.insert(0, str(eg_master_dir))

from timeit import Timer

import easygraph as eg

t = Timer("print(eg)", "from __main__ import eg")
t.timeit(1)

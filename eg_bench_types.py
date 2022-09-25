#!/usr/bin/env python3

# from typing import Union
# MethodName = 'Union[str, tuple[str, str]]'

from typing import NamedTuple
from datetime import datetime


MethodName = str | tuple[str, str]

# datetime when the benchmark was run
DTForTools = NamedTuple(
    'DTForTools', [('eg', datetime), ('nx', datetime), ('ceg', datetime)]
)

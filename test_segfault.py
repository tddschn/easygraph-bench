#!/usr/bin/env python3

import subprocess
import shlex

subprocess.run(
    shlex.join(['./bench_eco.py', '-D', '-G', 'new', '-a', '-N']),
    shell=True,
    check=True,
)

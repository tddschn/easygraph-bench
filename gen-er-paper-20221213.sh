#!/usr/bin/env bash

DIR_NAME='er-paper-20221213'


./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '50000' --edges '60000'

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '500000' --edges '70000'

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '1000000' --edges '80000'

#!/usr/bin/env bash

DIR_NAME='er-paper-20221221'


./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '100000' --edges '50000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '100000' --edges '100000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '100000' --edges '200000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '100000' --edges '500000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '1000000' --edges '50000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '1000000' --edges '100000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '1000000' --edges '200000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '1000000' --edges '500000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '1000000' --edges '1000000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '1000000' --edges '2000000' --sparse

./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '1000000' --edges '5000000' --sparse

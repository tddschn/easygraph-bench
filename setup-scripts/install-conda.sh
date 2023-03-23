#!/usr/bin/env bash

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
# https://docs.anaconda.com/anaconda/install/silent-mode/

eval "$($HOME/miniconda/bin/conda shell.zsh hook)"
conda init zsh

#!/usr/bin/env bash

# set default path to Easy-Graph repo dir
repo_path="${1:-$HOME/Easy-Graph}"

# remember current directory
orig_dir="$(pwd)"

# print help message if user passes --help flag
if [[ $1 == "--help" ]]; then
  echo "Usage: ./update_easygraph.sh [PATH]"
  echo "Update the Easy-Graph repo located at PATH."
  echo "If PATH is not specified, defaults to ~/Easy-Graph."
  exit 0
fi

# cd to repo dir and update using git pull
cd "$repo_path" || exit
before=$(git rev-parse HEAD)
git pull > /dev/null
after=$(git rev-parse HEAD)

# if updates are pulled, run setup.py install and inform user
if [[ "$before" != "$after" ]]; then
  echo "Updates pulled from Easy-Graph repo."
  python3 setup.py install
else
  echo "No updates available for Easy-Graph repo."
fi

# change back to original directory
cd "$orig_dir" || exit

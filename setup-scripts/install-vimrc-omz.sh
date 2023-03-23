#!/usr/bin/env bash

git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime && sh ~/.vim_runtime/install_awesome_vimrc.sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
curl -s https://gist.githubusercontent.com/tddschn/5c46a2070962a168d2f367d86c7a9d98/raw/376bfcbed7cafd0dcd01307604998aa7943b90bf/.zshrc >~/.zshrc

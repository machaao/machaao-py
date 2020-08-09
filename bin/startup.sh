#!/bin/sh

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
MACHAAO_FILE_PATH="${PATH}:${SOURCE_DIR}/machaao"
MACHAAO_FILE="${SOURCE_DIR}/machaao"

export PATH=$MACHAAO_FILE

chmod +x $MACHAAO_FILE

if [[ $0 == "bash" ]]; then
    echo "export PATH=${MACHAAO_FILE}" >> ~/.bashrc

elif [[ $0 == "ksh" ]]; then
    echo "export PATH=${MACHAAO_FILE}" >> ~/.kshrc

elif [[ $0 == "zsh" ]]; then
    echo "export PATH=${MACHAAO_FILE}" >> ~/.zshrc

fi
#!/bin/bash

chmod +x gptea.sh
{ echo ""; echo "# ChatGP-Tea"; echo "alias gptea=\"source $(pwd)/gptea.sh\""; echo ""; } >> "$HOME/.bashrc"
mkdir "generated-scripts"
mkdir "conversations"
source "$HOME/.bashrc"
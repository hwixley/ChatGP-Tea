#!/bin/bash

chmod +x gptea.sh
echo "" >> ~/.bashrc
echo "alias gptea=\"source $(pwd)/gptea.sh\"" >> ~/.bashrc
mkdir "generated-scripts"
mkdir "conversations"
source ~/.bashrc
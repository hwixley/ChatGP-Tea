#!/bin/bash

# get regex and string input from user
read -p "Enter regular expression: " regex
read -p "Enter string: " string

# check for match
if [[ $string =~ $regex ]]; then
  echo "Match found!"
else
  echo "No match found."
fi

# exit
exit 0
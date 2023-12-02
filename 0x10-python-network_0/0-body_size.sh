#!/bin/bash
# store the url in a variable
echo $(curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')

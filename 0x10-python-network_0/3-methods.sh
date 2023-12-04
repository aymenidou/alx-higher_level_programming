#!/bin/bash
# get all allowed http methods
curl -s -I "$1" | grep -i Allow | cut -d " " -f 2-

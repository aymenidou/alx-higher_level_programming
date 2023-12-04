#!/bin/bash
# get all allowed http methods
curl -s -I "secretsoftech.tech" | grep -i Allow | cut -d " " -f 2-

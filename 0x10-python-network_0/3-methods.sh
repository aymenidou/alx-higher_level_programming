#!/bin/bash
# get all allowed http methods
curl -s -I "secretsoftech.tech" | grep -i Allow | sed 's/Allow: //i'

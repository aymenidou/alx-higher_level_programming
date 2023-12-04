#!/bin/bash
# send post request to url in argument with file as param
curl -s -L -X POST "$1" -d "@$2" -H "Content-Type: application/json"

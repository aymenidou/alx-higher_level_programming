#!/bin/bash
# send post request to url in argument with file as param
curl -s -L -X POST "$1" --form "fileupload=@$2"

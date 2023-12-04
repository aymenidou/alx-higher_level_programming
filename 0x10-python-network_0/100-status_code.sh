#!/bin/bash
# get the http status only
curl -s -o /dev/null -w %{http_code} $1

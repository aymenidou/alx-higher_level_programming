#!/bin/bash
# get response_code check if it's 200 then display the body of the page
response_code=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ $response_code -eq 200 ] && curl -s "$1"

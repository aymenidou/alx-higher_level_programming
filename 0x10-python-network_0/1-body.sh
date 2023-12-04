#!/bin/bash
# get response_code check if it's 200 then display the body of the page
curl -sLX GET "$1"

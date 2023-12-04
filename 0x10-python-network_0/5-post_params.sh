#!/bin/bash
# send post request to url in argument
curl -s -L -X POST "$1" --data "email=test@gmail.com&subject=I will always be here for PLD"

#!/bin/bash
# send get request with param X-School-User-Id
curl -s -L -X  GET "$1" -H "X-School-User-Id:98"

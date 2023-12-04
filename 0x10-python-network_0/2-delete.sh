#!/bin/bash
# sends a DELETE request to the URL in the &st argument
curl -sXL DELETE "$1"

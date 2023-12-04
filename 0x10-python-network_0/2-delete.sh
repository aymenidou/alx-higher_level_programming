#!/bin/bash
# sends a DELETE request to the URL in the &st argument
curl -sLX DELETE "$1"

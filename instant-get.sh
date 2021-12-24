#!/bin/bash

echo "$(date +%Y/%m/%d-%H:%M:%S) $(sensors | grep "^Package" | awk '{print $4}' | xargs)"

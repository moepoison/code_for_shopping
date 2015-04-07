#!/bin/bash
# first argument is file name
# second arg is target website
run_dir=$( dirname "${BASH_SOURCE[0]}" )
cd ${run_dir}
./bin/python start_crawler.py "$1"



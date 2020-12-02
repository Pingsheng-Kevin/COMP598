#!/usr/bin/env bash
python check_duplicates.py ../data/20201117_conservative_hot.json ../data/20201117_conservative_new.json
python check_duplicates.py ../data/20201117_politics_hot.json ../data/20201117_politics_new.json
python check_duplicates.py ../data/20201121_conservative_hot.json ../data/20201121_conservative_new.json
python check_duplicates.py ../data/20201121_politics_hot.json ../data/20201121_politics_new.json
python check_duplicates.py ../data/20201122_conservative_hot.json ../data/20201122_conservative_new.json
python check_duplicates.py ../data/20201122_politics_hot.json ../data/20201122_politics_new.json
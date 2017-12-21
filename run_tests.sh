#!/usr/bin/env bash

nosetests -v --nocapture tests/test_database.py
nosetests -v --nocapture tests/test_geothoughts.py
nosetests -v --nocapture tests/test_main.py

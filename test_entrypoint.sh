#!/bin/bash
python3 app/manage.py runserver &

python3 test.py

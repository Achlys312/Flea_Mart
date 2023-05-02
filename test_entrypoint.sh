#!/bin/bash
python3 app/manage.py runserver &
python3 manage.py test
#python3 test.py

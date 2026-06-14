#!/bin/bash

rm db.sqlite3
rm -rf ./partapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations partapi
python3 manage.py migrate partapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens


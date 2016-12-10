#!/bin/sh
#git clone https://github.com/a0919610611/Library.git Library
python3 /database_check.py
while [[ $? != 0  ]] ; do
        sleep 5; echo "*** Waiting for database container ..."
            python3 /database_check.py 
        done
cd Library
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations api
python3 manage.py migrate
python3 init.py
uwsgi --ini uwsgi.ini


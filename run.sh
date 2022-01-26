#!/bin/bash

function trap_ctrlc ()
{
    docker-compose down
    exit 2
}

trap "trap_ctrlc" 2

rm polls/migrations/00*
rm venv/lib/python3.10/site-packages/organizations/migrations/00*

python manage.py makemigrations polls

docker-compose -f docker-compose.yml -f docker-compose.local.yml down && docker-compose -f docker-compose.yml -f docker-compose.local.yml up -d postgres

sleep 2

python manage.py migrate
python manage.py runserver

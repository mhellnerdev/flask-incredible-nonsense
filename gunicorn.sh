#!/bin/sh

mkdir -p ./log/ && touch $_/gunicorn-access.log

gunicorn --bind 0.0.0.0:5000 -w 3 --access-logfile ./log/gunicorn-access.log app:app
#!/bin/bash

set -ex

# create the virtual environment
pipenv run python --version

DBNAME=cleaning
# https://stackoverflow.com/a/18389184/358804
echo "SELECT 'CREATE DATABASE $DBNAME' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$DBNAME')\gexec" | psql postgresql://postgres:postgres@db

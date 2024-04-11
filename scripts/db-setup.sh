#!/bin/sh


export PGUSER="postgres"

psql -c "CREATE DATABASE fk_commerce"


psql fkcommerce -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"

    
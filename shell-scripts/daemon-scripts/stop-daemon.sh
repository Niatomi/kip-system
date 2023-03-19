#!/bin/bash

pkill -9 -f main.py

cd ../..

docker-compose down

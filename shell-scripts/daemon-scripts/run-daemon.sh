#!/bin/bash

cd $base_path

docker-compose up -d

cd backend

source bin/activate

cd src

python main.py &

cd $base_path/frontend/kip-app

ng serve

#!/bin/bash

cd $base_path

cd backend

python -m venv .

source bin/activate

pip install --upgrade pip

pip install wheel

pip install -r requirements.txt

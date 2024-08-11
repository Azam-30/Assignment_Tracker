#!/bin/bash
set -e

echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Running collectstatic..."
python3 manage.py collectstatic --noinput

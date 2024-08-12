#!/bin/bash
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput

echo "Applying database migrations..."
python3.9 manage.py migrate

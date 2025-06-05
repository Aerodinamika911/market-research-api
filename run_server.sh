#!/bin/bash

set -e

# Add required packages if missing
grep -qxF 'flask' requirements.txt || echo 'flask' >> requirements.txt
grep -qxF 'gunicorn' requirements.txt || echo 'gunicorn' >> requirements.txt

# Install dependencies
pip install -r requirements.txt

# Download ngrok if not present
if [ ! -x ./ngrok ]; then
  echo "Downloading ngrok..."
  wget -q https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
  unzip -o ngrok-stable-linux-amd64.zip
  chmod +x ngrok
  rm ngrok-stable-linux-amd64.zip
  echo "If you haven't run './ngrok authtoken <YOUR_NGROK_TOKEN>' before, do it now."
fi

# Start Gunicorn server
echo "Starting backend server with Gunicorn..."
nohup gunicorn --bind 0.0.0.0:5000 market_research_server:app > server.log 2>&1 &

# Wait for Gunicorn to start
sleep 5

# Start ngrok
echo "Starting ngrok..."
./ngrok http 5000

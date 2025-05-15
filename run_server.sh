#!/bin/bash
pip install -r requirements.txt
nohup gunicorn --bind 0.0.0.0:5000 market_research_server:app &
./ngrok http 5000

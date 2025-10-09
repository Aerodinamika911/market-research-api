from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
socketio = SocketIO(app)
API_BASE_URL = "https://your-ngrok-url.ngrok.io"  # Update this for your deployment!

ENDPOINTS = [
    {"path": "/extractBehavioralPatterns", "label": "Extract Behavioral Patterns"},
    {"path": "/generateStatisticalModels", "label": "Generate Statistical Models"},
    {"path": "/compareMarketSegments", "label": "Compare Market Segments"},
    {"path": "/trackCompetitorMovements", "label": "Track Competitor Movements"},
    {"path": "/forecastMarketTrends", "label": "Forecast Market Trends"},
    {"path": "/synthesizeVoiceOfCustomer", "label": "Synthesize Voice of Customer"},
    {"path": "/runSocialListening", "label": "Run Social Listening"},
    {"path": "/visualizeInsight", "label": "Visualize Insight"},
    {"path": "/generateExecutiveSummary", "label": "Generate Executive Summary"},
    {"path": "/frameStrategicQuestion", "label": "Frame Strategic Question"},
    {"path": "/learnFromPastDecisions", "label": "Learn From Past Decisions"},
    {"path": "/mapIntuitionToAction", "label": "Map Intuition To Action"},
]

@app.route('/')
def index():
    return render_template('dashboard_advanced.html', endpoints=ENDPOINTS)

@socketio.on('run_api')
def handle_run_api(data):
    endpoint = data.get('endpoint')
    if not endpoint:
        emit('api_result', {'error': 'No endpoint specified'})
        return
    url = API_BASE_URL + endpoint
    try:
        response = requests.post(url)
        emit('api_result', {
            'endpoint': endpoint,
            'result': response.json(),
            'raw': response.text,
            'status_code': response.status_code
        })
    except Exception as e:
        emit('api_result', {'endpoint': endpoint, 'error': str(e), 'status_code': 500})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
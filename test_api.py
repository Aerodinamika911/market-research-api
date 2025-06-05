import pytest
import requests

# Replace this with your actual ngrok URL after running the server
BASE_URL = "https://your-ngrok-url.ngrok.io"

endpoints = [
    "/extractBehavioralPatterns",
    "/generateStatisticalModels",
    "/compareMarketSegments",
    "/trackCompetitorMovements",
    "/forecastMarketTrends",
    "/synthesizeVoiceOfCustomer",
    "/runSocialListening",
    "/visualizeInsight",
    "/generateExecutiveSummary",
    "/frameStrategicQuestion",
    "/learnFromPastDecisions",
    "/mapIntuitionToAction"
]

@pytest.mark.parametrize("endpoint", endpoints)
def test_post_endpoints(endpoint):
    url = BASE_URL + endpoint
    try:
        response = requests.post(url)
        assert response.status_code == 200, f"{endpoint} returned status {response.status_code}"
        json_data = response.json()
        assert "success" in json_data.get("status", "").lower(), f"{endpoint} response: {json_data}"
    except Exception as e:
        pytest.fail(f"Request to {endpoint} failed with error: {e}")

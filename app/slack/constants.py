from app.config import SLACK_TOKEN

PLATFORM = "SLACK"

SLACK_HEADERS = {"Content-Type": "application/json", "Authorization": "Bearer " + SLACK_TOKEN}

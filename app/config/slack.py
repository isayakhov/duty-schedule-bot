import os

SLACK_TOKEN = os.getenv("SLACK_TOKEN", "")

SLACK_URL = os.getenv("SLACK_URL", "https://slack.com/api/chat.postMessage")

WEB_SERVER_NAME = os.getenv("APP_NAME", "Duty Schedule Bot")
WEB_SERVER_HOST = os.getenv("WEB_SERVER_HOST", "0.0.0.0")
WEB_SERVER_PORT = int(os.getenv("WEB_SERVER_PORT", "8000"))
WEB_SERVER_DEBUG = bool(int(os.getenv("APP_DEBUG", "0")))

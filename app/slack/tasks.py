import logging

import requests

from app.common import handlers as common_handlers
from app.common.cache import cache
from app.config import SLACK_URL

from .constants import PLATFORM, SLACK_HEADERS

logger = logging.getLogger(__name__)


def set_schedule():
    logger.info("Started to set up schedule")

    for chat_id in cache.get_chats_by_people(PLATFORM):
        requests.post(
            url=SLACK_URL,
            headers=SLACK_HEADERS,
            json={"channel": chat_id, "text": common_handlers.set_schedule(PLATFORM, chat_id), "link_names": 1},
        )

    logger.info("Finished to set up schedule")


def remind(tomorrow: bool):
    logger.info("Started to remind schedule")

    for chat_id in cache.get_chats_by_schedules(PLATFORM):
        message = common_handlers.remind(PLATFORM, chat_id, tomorrow)
        if message:
            requests.post(
                url=SLACK_URL, headers=SLACK_HEADERS, json={"channel": chat_id, "text": message, "link_names": 1}
            )

    logger.info("Finished to remind schedule")

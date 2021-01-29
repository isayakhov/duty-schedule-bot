import logging

from telegram import Bot

from app.common import handlers as common_handlers
from app.common.cache import cache
from app.config import PLATFORM, TELEGRAM_TOKEN

logger = logging.getLogger(__name__)


def set_schedule():
    logger.info("Started to set up schedule")

    bot = Bot(TELEGRAM_TOKEN)

    for chat_id in cache.get_chats_by_people(PLATFORM):
        bot.get_chat(chat_id).send_message(common_handlers.set_schedule(PLATFORM, chat_id))

    logger.info("Finished to set up schedule")


def remind(tomorrow: bool):
    logger.info("Started to remind schedule")

    bot = Bot(TELEGRAM_TOKEN)

    for chat_id in cache.get_chats_by_schedules(PLATFORM):
        bot.get_chat(chat_id).send_message(common_handlers.remind(PLATFORM, chat_id, tomorrow))

    logger.info("Finished to remind schedule")

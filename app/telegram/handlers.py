import logging

from app.common import exceptions
from app.common import handlers as common_handlers
from app.common.constants import HELP_ADD_TEXT, HELP_NO_SCHEDULE_TEXT, HELP_REMOVE_TEXT, HELP_START_TEXT
from app.config import PLATFORM

logger = logging.getLogger(__name__)


def start(update, context):
    assert context is not None

    logger.info("Trying to show help message")

    update.message.reply_text(HELP_START_TEXT)

    logger.info("Finish start handler")


def create_schedule(update, context):
    assert context is not None

    logger.info("Trying to create schedule")

    chat_id = update.message.chat_id

    schedule = common_handlers.set_schedule(PLATFORM, chat_id)
    if not schedule:
        schedule = HELP_NO_SCHEDULE_TEXT

    update.message.reply_text(schedule)

    logger.info("Finish create_schedule handler")


def show_schedule(update, context):
    assert context is not None
    logger.info("Trying to show schedule")

    chat_id = update.message.chat_id
    try:
        update.message.reply_text(common_handlers.get_schedule(PLATFORM, chat_id))
    except exceptions.ScheduleNotFound as exc:
        logger.warning("Can't show schedule")
        update.message.reply_text(exc.message)

    logger.info("Finish show_schedule handler")


def add_person(update, context):
    logger.info("Trying to add person to schedule")

    chat_id = update.message.chat_id
    try:
        username = str(context.args[0])
    except (IndexError, ValueError):
        logger.info("Can't add person to schedule")
        update.message.reply_text(HELP_ADD_TEXT)
        return

    try:
        update.message.reply_text(common_handlers.add_person(PLATFORM, chat_id, username))
    except (exceptions.IncorrectUsername, exceptions.UserAlreadyExists) as exc:
        update.message.reply_text(exc.message)

    logger.info("Finish add_person handler")


def remove_person(update, context):
    logger.info("Trying to remove person to schedule")

    chat_id = update.message.chat_id
    try:
        username = str(context.args[0])
    except (IndexError, ValueError):
        logger.info("Can't remove person to schedule")
        update.message.reply_text(HELP_REMOVE_TEXT)
        return

    try:
        update.message.reply_text(common_handlers.remove_person(PLATFORM, chat_id, username))
    except (exceptions.IncorrectUsername, exceptions.UserDoesNotExist) as exc:
        update.message.reply_text(exc.message)

    logger.info("Finish remove_person handler")


def error(update, context):
    logger.warning("Update '%s' caused error '%s'", update, context.error)

from unittest import mock

from app.common import constants, exceptions
from app.common import handlers as common_handlers
from app.config import PLATFORM
from app.telegram.handlers import add_person, create_schedule, error, remove_person, show_schedule, start


def test_start(tg_update, tg_context):
    start(tg_update, tg_context)

    tg_update.message.reply_text.assert_called_once()


def test_create_schedule(tg_update, tg_context, chat_id, username):
    common_handlers.add_person(PLATFORM, chat_id, username)
    create_schedule(tg_update, tg_context)

    tg_update.message.reply_text.assert_called_once()


def test_create_schedule_no_schedule(tg_update, tg_context):
    create_schedule(tg_update, tg_context)

    tg_update.message.reply_text.assert_called_once_with(constants.HELP_NO_SCHEDULE_TEXT)


def test_show_schedule(tg_update, tg_context, chat_id, username):
    common_handlers.add_person(PLATFORM, chat_id, username)
    common_handlers.set_schedule(PLATFORM, chat_id)

    show_schedule(tg_update, tg_context)

    tg_update.message.reply_text.assert_called_once()


def test_show_schedule_not_found(tg_update, tg_context, chat_id, username):
    common_handlers.add_person(PLATFORM, chat_id, username)
    show_schedule(tg_update, tg_context)

    tg_update.message.reply_text.assert_called_once_with(exceptions.ScheduleNotFound.default_message)


def test_add_person(tg_update, tg_context):
    add_person(tg_update, tg_context)

    tg_update.message.reply_text.assert_called_once()


def test_add_person_incorrect_context(tg_update):
    add_person(tg_update, mock.MagicMock(args=[]))

    tg_update.message.reply_text.assert_called_once_with(constants.HELP_ADD_TEXT)


def test_add_person_incorrect_username(tg_update):
    add_person(tg_update, mock.MagicMock(args=["BAD_NAME"]))

    tg_update.message.reply_text.assert_called_once_with(exceptions.IncorrectUsername.default_message)


def test_remove_person(tg_update, tg_context):
    remove_person(tg_update, tg_context)

    tg_update.message.reply_text.assert_called_once()


def test_remove_person_incorrect_context(tg_update):
    remove_person(tg_update, mock.MagicMock(args=[]))

    tg_update.message.reply_text.assert_called_once_with(constants.HELP_REMOVE_TEXT)


def test_remove_person_incorrect_username(tg_update):
    remove_person(tg_update, mock.MagicMock(args=["BAD_NAME"]))

    tg_update.message.reply_text.assert_called_once_with(exceptions.IncorrectUsername.default_message)


def test_error(mocker, tg_update, tg_context):
    logger_mock = mock.MagicMock(warning=mock.MagicMock())
    mocker.patch("app.telegram.handlers.logger", logger_mock)

    error(tg_update, tg_context)

    logger_mock.warning.assert_called_once()

from datetime import datetime

from app.common import handlers as common_handlers
from app.telegram.constants import PLATFORM
from app.telegram.tasks import remind, set_schedule


def test_set_schedule(mocker, tg_bot, chat_id, username):
    mocker.patch("app.telegram.tasks.Bot", tg_bot)

    common_handlers.add_person(PLATFORM, chat_id, username)

    set_schedule()

    assert tg_bot.called


def test_remind(mocker, tg_bot, chat_id, username):
    mocker.patch("app.telegram.tasks.Bot", tg_bot)

    common_handlers.add_person(PLATFORM, chat_id, username)
    common_handlers.set_schedule(PLATFORM, chat_id)
    remind(True)

    assert tg_bot.called


def test_remind_out_of_index(mocker, tg_bot, chat_id, username):
    mocker.patch("app.telegram.tasks.Bot", tg_bot)
    mocker.patch("app.common.handlers._get_today", return_value=datetime(year=2021, month=1, day=30))

    common_handlers.add_person(PLATFORM, chat_id, username)
    common_handlers.set_schedule(PLATFORM, chat_id)
    remind(False)

    assert not tg_bot.get_chat.called

from app.common.handlers import add_person
from app.config import PLATFORM
from app.telegram.tasks import remind, set_schedule


def test_set_schedule(mocker, tg_bot, chat_id, username):
    mocker.patch("app.telegram.tasks.Bot", tg_bot)

    add_person(PLATFORM, chat_id, username)

    set_schedule()

    assert tg_bot.called


def test_remind(mocker, tg_bot, chat_id, username):
    mocker.patch("app.telegram.tasks.Bot", tg_bot)

    add_person(PLATFORM, chat_id, username)
    set_schedule()
    remind(True)

    assert tg_bot.called

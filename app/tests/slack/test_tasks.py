from datetime import datetime

from app.common import handlers as common_handlers
from app.slack.constants import PLATFORM
from app.slack.tasks import remind, set_schedule


def test_set_schedule(mocker, requests_post, chat_id, username):
    mocker.patch("app.slack.tasks.requests.post", requests_post)

    common_handlers.add_person(PLATFORM, chat_id, username)

    set_schedule()

    assert requests_post.called


def test_remind(mocker, requests_post, chat_id, username):
    mocker.patch("app.slack.tasks.requests.post", requests_post)
    mocker.patch("app.common.handlers._get_today", return_value=datetime(year=2021, month=1, day=27))

    common_handlers.add_person(PLATFORM, chat_id, username)
    common_handlers.set_schedule(PLATFORM, chat_id)
    remind(True)

    assert requests_post.called


def test_remind_out_of_index(mocker, requests_post, chat_id, username):
    mocker.patch("app.slack.tasks.requests.post", requests_post)
    mocker.patch("app.common.handlers._get_today", return_value=datetime(year=2021, month=1, day=30))

    common_handlers.add_person(PLATFORM, chat_id, username)
    common_handlers.set_schedule(PLATFORM, chat_id)
    remind(False)

    assert not requests_post.called

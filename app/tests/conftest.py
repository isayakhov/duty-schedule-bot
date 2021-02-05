# pylint: disable=redefined-outer-name

from unittest import mock

import pytest
from fastapi.testclient import TestClient

from app.common import cache


@pytest.fixture(autouse=True, scope="function")
def clear_cache():
    # pylint: disable=protected-access
    cache._redis_cli.flushall()  # noqa


@pytest.fixture
def chat_id(faker):
    return faker.pystr()


@pytest.fixture
def username(faker):
    return f"@{faker.name()}"


@pytest.fixture
def tg_update(chat_id):
    return mock.MagicMock(message=mock.MagicMock(chat_id=chat_id, reply_text=mock.MagicMock()))


@pytest.fixture
def tg_context(username):
    return mock.MagicMock(args=[username])


@pytest.fixture
def tg_bot():
    # bot.get_chat(chat_id).send_message()
    return mock.MagicMock(
        get_chat=mock.MagicMock(return_value=mock.MagicMock(send_message=mock.MagicMock(return_value=None)))
    )


@pytest.fixture
def requests_post():
    return mock.MagicMock()


@pytest.fixture
def slack_web_client():
    # pylint: disable=import-outside-toplevel
    from app.slack.run_bot import app

    return TestClient(app)

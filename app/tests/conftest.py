# pylint: disable=redefined-outer-name

from unittest import mock

import pytest

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
    return mock.MagicMock()

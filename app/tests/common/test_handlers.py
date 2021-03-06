import calendar
from datetime import datetime

import pytest

from app.common import constants, exceptions, handlers

_PLATFORM = "test"


def test_get_schedule(chat_id, username):
    handlers.add_person(_PLATFORM, chat_id, username)
    handlers.set_schedule(_PLATFORM, chat_id)

    assert handlers.get_schedule(_PLATFORM, chat_id) == "\n".join(
        f"{calendar.day_name[idx]}: {username}" for idx in range(5)
    )


def test_get_schedule_not_found(chat_id):
    with pytest.raises(exceptions.ScheduleNotFound) as exc_info:
        handlers.get_schedule(_PLATFORM, chat_id)

    assert exc_info.value.code == exceptions.ScheduleNotFound.code


def test_add_person(chat_id, username):
    assert handlers.add_person(_PLATFORM, chat_id, username) == constants.PERSON_ADDED.format(username=username)


def test_add_person_incorrect_username(faker, chat_id):
    with pytest.raises(exceptions.IncorrectUsername) as exc_info:
        handlers.add_person(_PLATFORM, chat_id, faker.name())

    assert exc_info.value.code == exceptions.IncorrectUsername.code


def test_add_person_user_already_exists(chat_id, username):
    handlers.add_person(_PLATFORM, chat_id, username)
    with pytest.raises(exceptions.UserAlreadyExists) as exc_info:
        handlers.add_person(_PLATFORM, chat_id, username)

    assert exc_info.value.code == exceptions.UserAlreadyExists.code


def test_remove_person(chat_id, username):
    handlers.add_person(_PLATFORM, chat_id, username)

    assert handlers.remove_person(_PLATFORM, chat_id, username) == constants.PERSON_REMOVED.format(username=username)


def test_remove_person_incorrect_username(faker, chat_id):
    with pytest.raises(exceptions.IncorrectUsername) as exc_info:
        handlers.remove_person(_PLATFORM, chat_id, faker.name())

    assert exc_info.value.code == exceptions.IncorrectUsername.code


def test_remove_person_user_does_not_exist(chat_id, username):
    with pytest.raises(exceptions.UserDoesNotExist) as exc_info:
        handlers.remove_person(_PLATFORM, chat_id, username)

    assert exc_info.value.code == exceptions.UserDoesNotExist.code


def test_set_schedule(chat_id, username):
    handlers.add_person(_PLATFORM, chat_id, username)

    assert_msg = constants.WEEK_SCHEDULE.format(
        schedule="\n".join(f"{calendar.day_name[idx]}: {username}" for idx in range(5))
    )
    assert handlers.set_schedule(_PLATFORM, chat_id) == assert_msg


def test_set_schedule_no_people(faker):
    assert handlers.set_schedule(faker.pystr(), faker.pystr()) is None


@pytest.mark.parametrize(
    "msg,date,is_today",
    [
        (constants.MORNING_REMINDER, datetime(year=2021, month=1, day=28), False),
        (constants.EVENING_REMINDER, datetime(year=2021, month=1, day=27), True),
    ],
)
def test_remind(mocker, msg, date, is_today, chat_id, username):
    handlers.add_person(_PLATFORM, chat_id, username)
    handlers.set_schedule(_PLATFORM, chat_id)

    mocker.patch("app.common.handlers._get_today", return_value=date)

    assert handlers.remind(_PLATFORM, chat_id, is_today) == msg.format(username=username)


def test_remind_out_of_limit(mocker, chat_id):
    handlers.set_schedule(_PLATFORM, chat_id)

    mocker.patch("app.common.handlers._get_today", return_value=datetime(year=2021, month=1, day=30))

    assert handlers.remind(_PLATFORM, chat_id, False) is None


def test_remind_out_of_index(mocker, chat_id, username):
    handlers.set_schedule(_PLATFORM, chat_id)

    mocker.patch("app.common.handlers._get_today", return_value=datetime(year=2021, month=1, day=27))
    mocker.patch("app.common.handlers.cache.get_schedule", return_value=[username])

    assert handlers.remind(_PLATFORM, chat_id, False) == constants.MORNING_REMINDER.format(username=username)


def test_get_today():
    # pylint: disable=protected-access
    assert handlers._get_today().day == datetime.today().day

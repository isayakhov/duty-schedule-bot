from app.common import constants, exceptions
from app.common import handlers as common_handlers
from app.slack.constants import PLATFORM


def test_start(slack_web_client):
    response = slack_web_client.post("/start")

    assert response.status_code == 200
    assert response.json() == {"text": constants.HELP_START_TEXT, "link_names": 1}


def test_create_schedule(slack_web_client, chat_id, username):
    common_handlers.add_person(PLATFORM, chat_id, username)

    response = slack_web_client.post("/create", data={"channel_id": chat_id})

    assert response.status_code == 200
    assert "text" in response.json()


def test_create_schedule_no_schedule(slack_web_client, chat_id):
    response = slack_web_client.post("/create", data={"channel_id": chat_id})

    assert response.status_code == 200
    assert response.json() == {"text": constants.HELP_NO_SCHEDULE_TEXT, "link_names": 1}


def test_show_schedule(slack_web_client, chat_id, username):
    common_handlers.add_person(PLATFORM, chat_id, username)
    common_handlers.set_schedule(PLATFORM, chat_id)

    response = slack_web_client.post("/week", data={"channel_id": chat_id})

    assert response.status_code == 200
    assert "text" in response.json()


def test_show_schedule_not_found(slack_web_client, chat_id, username):
    common_handlers.add_person(PLATFORM, chat_id, username)

    response = slack_web_client.post("/week", data={"channel_id": chat_id})

    assert response.status_code == 200
    assert response.json() == {"text": exceptions.ScheduleNotFound.default_message, "link_names": 1}


def test_add_person(slack_web_client, chat_id, username):
    response = slack_web_client.post("/add", data={"channel_id": chat_id, "text": username})

    assert response.status_code == 200
    assert "text" in response.json()


def test_add_person_incorrect_username(slack_web_client, chat_id):
    response = slack_web_client.post("/add", data={"channel_id": chat_id, "text": "BAD_NAME"})

    assert response.status_code == 200
    assert response.json() == {"text": exceptions.IncorrectUsername.default_message, "link_names": 1}


def test_remove_person(slack_web_client, chat_id, username):
    slack_web_client.post("/add", data={"channel_id": chat_id, "text": username})
    response = slack_web_client.post("/remove", data={"channel_id": chat_id, "text": username})

    assert response.status_code == 200
    assert "text" in response.json()


def test_remove_person_user_does_not_exist(slack_web_client, chat_id, username):
    response = slack_web_client.post("/remove", data={"channel_id": chat_id, "text": username})

    assert response.status_code == 200
    assert response.json() == {"text": exceptions.UserDoesNotExist.default_message, "link_names": 1}


def test_remove_person_incorrect_username(slack_web_client, chat_id):
    response = slack_web_client.post("/remove", data={"channel_id": chat_id, "text": "BAD_NAME"})

    assert response.status_code == 200
    assert response.json() == {"text": exceptions.IncorrectUsername.default_message, "link_names": 1}

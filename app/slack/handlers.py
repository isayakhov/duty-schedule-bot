import logging

from fastapi import APIRouter, Form
from pydantic import BaseModel

from app.common import exceptions
from app.common import handlers as common_handlers
from app.common.constants import HELP_NO_SCHEDULE_TEXT, HELP_START_TEXT

from .constants import PLATFORM

logger = logging.getLogger(__name__)

router = APIRouter()


class HandlerResponse(BaseModel):
    text: str
    link_names: int = 1


@router.post("/start", response_model=HandlerResponse)
def start():
    logger.info("Trying to show help message")

    logger.info("Finish help handler")

    return HandlerResponse(text=HELP_START_TEXT)


@router.post("/create", response_model=HandlerResponse)
def create_schedule(chat_id: str = Form(..., alias="channel_id")):
    logger.info("Trying to create schedule")

    schedule = common_handlers.set_schedule(PLATFORM, chat_id)
    if not schedule:
        schedule = HELP_NO_SCHEDULE_TEXT

    logger.info("Finish create_schedule handler")

    return HandlerResponse(text=schedule)


@router.post("/week", response_model=HandlerResponse)
def show_schedule(chat_id: str = Form(..., alias="channel_id")):
    logger.info("Trying to show schedule")

    try:
        message = common_handlers.get_schedule(PLATFORM, chat_id)
    except exceptions.ScheduleNotFound as exc:
        logger.warning("Can't show schedule")
        message = exc.message

    logger.info("Finish show_schedule handler")

    return HandlerResponse(text=message)


@router.post("/add", response_model=HandlerResponse)
def add_person(chat_id: str = Form(..., alias="channel_id"), username: str = Form(..., alias="text")):
    logger.info("Trying to add person to schedule")

    try:
        message = common_handlers.add_person(PLATFORM, chat_id, username)
    except (exceptions.IncorrectUsername, exceptions.UserAlreadyExists) as exc:
        message = exc.message

    logger.info("Finish add_person handler")

    return HandlerResponse(text=message)


@router.post("/remove", response_model=HandlerResponse)
def remove_person(chat_id: str = Form(..., alias="channel_id"), username: str = Form(..., alias="text")):
    logger.info("Trying to remove person to schedule")

    try:
        message = common_handlers.remove_person(PLATFORM, chat_id, username)
    except (exceptions.IncorrectUsername, exceptions.UserDoesNotExist) as exc:
        message = exc.message

    logger.info("Finish remove_person handler")

    return HandlerResponse(text=message)

from typing import Optional


class DutyError(Exception):
    code = "INTERNAL_ERROR"
    default_message = "An internal error occurred."

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.default_message
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}(" f"code='{self.code}'," f" message='{self.message}'," f")"


class ScheduleNotFound(DutyError):
    code = "SCHEDULE_NOT_FOUND"
    default_message = "Schedule for given chat_id not found"


class UserAlreadyExists(DutyError):
    code = "USER_ALREADY_EXISTS"
    default_message = "User with given username already exists in schedule"


class IncorrectUsername(DutyError):
    code = "INCORRECT_USERNAME"
    default_message = "Incorrect username. Valid format: @username"


class UserDoesNotExist(DutyError):
    code = "USER_DOES_NOT_EXIST"
    default_message = "User for given chat_id does not exist"

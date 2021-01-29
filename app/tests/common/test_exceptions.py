from app.common.exceptions import DutyError


def test_duty_error():
    msg = "Custom message"
    exc = DutyError(message=msg)

    assert repr(exc) == f"DutyError(code='{DutyError.code}', message='{msg}',)"

from app import errors


def test_error_subclasses_and_isinstance():
    assert issubclass(errors.AuthError, errors.AppError)
    assert issubclass(errors.ValidationError, errors.AppError)
    assert issubclass(errors.RepositoryError, errors.AppError)


def test_errors_can_be_raised_and_caught():
    try:
        raise errors.ValidationError("bad input")
    except errors.AppError as exc:
        assert isinstance(exc, errors.ValidationError)
        assert str(exc) == "bad input"

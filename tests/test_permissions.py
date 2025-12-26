import pytest
from app.permissions import has_permission


def test_has_permission_admin():
    assert has_permission("admin", "any_action") is True


def test_has_permission_user_read():
    assert has_permission("user", "read") is True


def test_has_permission_user_write():
    assert has_permission("user", "write") is False


def test_has_permission_guest():
    assert has_permission("guest", "read") is False
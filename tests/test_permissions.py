from app.permissions import has_permission


def test_admin_has_all_permissions():
    assert has_permission("admin", "read") is True
    assert has_permission("admin", "write") is True
    assert has_permission("admin", "delete") is True


def test_user_read_only():
    assert has_permission("user", "read") is True
    assert has_permission("user", "write") is False


def test_unknown_roles_and_case_sensitivity():
    assert has_permission("guest", "read") is False
    assert has_permission("user", "Read") is False

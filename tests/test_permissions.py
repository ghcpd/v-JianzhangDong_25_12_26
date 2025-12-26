import unittest
from app.permissions import has_permission


class TestPermissions(unittest.TestCase):

    def test_admin_has_all_permissions(self):
        self.assertTrue(has_permission("admin", "delete"))
        self.assertTrue(has_permission("admin", "read"))

    def test_user_read_allowed(self):
        self.assertTrue(has_permission("user", "read"))

    def test_user_other_denied(self):
        self.assertFalse(has_permission("user", "write"))

    def test_unknown_role_denied(self):
        self.assertFalse(has_permission("guest", "read"))

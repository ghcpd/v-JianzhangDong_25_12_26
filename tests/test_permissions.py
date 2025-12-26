import unittest
from app.permissions import has_permission


class TestPermissions(unittest.TestCase):

    def test_admin_has_all_permissions(self):
        """Test that admin has all permissions"""
        self.assertTrue(has_permission("admin", "read"))
        self.assertTrue(has_permission("admin", "write"))
        self.assertTrue(has_permission("admin", "delete"))
        self.assertTrue(has_permission("admin", "execute"))

    def test_user_can_read(self):
        """Test that user can read"""
        self.assertTrue(has_permission("user", "read"))

    def test_user_cannot_write(self):
        """Test that user cannot write"""
        self.assertFalse(has_permission("user", "write"))

    def test_user_cannot_delete(self):
        """Test that user cannot delete"""
        self.assertFalse(has_permission("user", "delete"))

    def test_user_cannot_execute(self):
        """Test that user cannot execute"""
        self.assertFalse(has_permission("user", "execute"))

    def test_guest_cannot_read(self):
        """Test that guest has no permissions"""
        self.assertFalse(has_permission("guest", "read"))

    def test_guest_cannot_write(self):
        """Test that guest cannot write"""
        self.assertFalse(has_permission("guest", "write"))

    def test_guest_cannot_delete(self):
        """Test that guest cannot delete"""
        self.assertFalse(has_permission("guest", "delete"))

    def test_unknown_role_has_no_permissions(self):
        """Test that unknown roles have no permissions"""
        self.assertFalse(has_permission("superuser", "read"))
        self.assertFalse(has_permission("moderator", "write"))

    def test_unknown_action(self):
        """Test unknown actions"""
        self.assertFalse(has_permission("user", "unknown_action"))
        # Admin can perform any action, even unknown ones
        self.assertTrue(has_permission("admin", "unknown_action"))

    def test_admin_with_unknown_action(self):
        """Test that admin can perform any action"""
        self.assertTrue(has_permission("admin", "custom_action"))

    def test_case_sensitivity(self):
        """Test role and action case sensitivity"""
        # Role is case-sensitive
        self.assertFalse(has_permission("Admin", "read"))
        # Action is case-sensitive (must be exactly "read")
        self.assertFalse(has_permission("user", "Read"))
        # Both must match exactly
        self.assertFalse(has_permission("USER", "read"))


if __name__ == "__main__":
    unittest.main()

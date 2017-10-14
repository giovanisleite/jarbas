from django.test import TestCase

from jarbas.dashboard.sites import DummyUser


class TestDummyUser(TestCase):

    def setUp(self):
        self.user = DummyUser()

    def test_has_module_perms(self):
        self.assertTrue(self.user.has_module_perms('chamber_of_deputies'))
        self.assertFalse(self.user.has_module_perms('api'))
        self.assertFalse(self.user.has_module_perms('dashboard'))
        self.assertFalse(self.user.has_module_perms('frontend'))

    def test_has_perm(self):
        self.assertTrue(self.user.has_perm('chamber_of_deputies.change_reimbursement'))
        self.assertFalse(self.user.has_perm('chamber_of_deputies.add_reimbursement'))
        self.assertFalse(self.user.has_perm('chamber_of_deputies.delete_reimbursement'))

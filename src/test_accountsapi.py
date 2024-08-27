import unittest
from accountsapi import get_random_first_name, get_random_family_name, get_random_dob, get_random_account_balance, get_random_classifier, get_random_date, get_random_account

class TestAccountsAPI(unittest.TestCase):
    def test_get_random_first_name(self):
        first_name = get_random_first_name()
        self.assertIn(first_name, ['John', 'Jane', 'Michael', 'Emily', 'David', 'Olivia'])

    def test_get_random_family_name(self):
        family_name = get_random_family_name()
        self.assertIn(family_name, ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis'])

    def test_get_random_dob(self):
        dob = get_random_dob()
        self.assertRegex(dob, r"\d{4}-\d{2}-\d{2}")

    def test_get_random_account_balance(self):
        account_balance = get_random_account_balance()
        self.assertGreaterEqual(account_balance, -3000)
        self.assertLessEqual(account_balance, 120000)

    def test_get_random_classifier(self):
        classifier = get_random_classifier()
        self.assertGreaterEqual(classifier, 1)
        self.assertLessEqual(classifier, 14)

    def test_get_random_date(self):
        date = get_random_date()
        self.assertRegex(date, r"\d{4}-\d{2}-\d{2}")

    def test_get_random_account(self):
        account = get_random_account()
        self.assertIsInstance(account, dict)
        self.assertIn('first_name', account)
        self.assertIn('family_name', account)
        self.assertIn('dob', account)
        self.assertIn('account_balance', account)
        self.assertIn('account_type', account)

if __name__ == '__main__':
    unittest.main()
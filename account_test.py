import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(50)
        
    def test_start_amount(self):
        self.assertEqual(50, self.account.get_balance())
    
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(100, self.account.get_balance())
        
    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)
        
    def test_withdraw(self):
        self.account.withdraw(20)
        self.assertEqual(30, self.account.get_balance())
    
    def test_withdraw_isufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(100)        

if __name__=="__main__":
    unittest.main()
        
       
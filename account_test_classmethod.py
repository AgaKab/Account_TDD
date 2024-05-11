import unittest
from account import Account

class TestAccount(unittest.TestCase):
    # def setUp(self):
    #     self.account = Account(50)
    
    @classmethod
    def setUpClass(cls):
        cls.account =Account(100)
        
    def test_1_start_amount(self):
        self.assertEqual(100, self.account.get_balance())
    
    def test_2_deposit(self):
        self.account.deposit(50)
        self.assertEqual(150, self.account.get_balance())
        
    def test_3_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)
        
    def test_4_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(100, self.account.get_balance())
    
    def test_5_withdraw_isufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)        

if __name__=="__main__":
    unittest.main()
        
       
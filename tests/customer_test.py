import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jack Jarvis", 6.50, 76, 0)
        self.customer2 = Customer("Methedone Mick", 2.50, 17, 8)
        self.pub = Pub("The Clansman", 200.00)
        self.drinks = [
            {"name": "Tennents",
            "price": 2 ,
            "alcohol level": 2
            },
            {"name": "whisky",
            "price": 4 ,
            "alcohol level": 2
            }
        ]


    def test_total_cash(self):
        sum = self.get_total_cash(self.customer)
        self.assertEqual(1000, sum)

    def test_remove_customer_cash(self):
        self.customer.remove_customer_cash(self.pub.drinks[0]["price"])
        cash = self.get_total_cash(self.purse)
        self.assertEqual(4.50, cash)
    
    def test_get_drunkennes(self):
        self.get_drunkenness(self)
        self.assertEqual(2,self.get_drukenness)
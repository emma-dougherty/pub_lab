import unittest
from src.pub import Pub
from src.customer import Customer




class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jack Jarvis", 6.50, 76)
        self.pub = Pub("The Clansman", 200.00)
        self.drinks = [
            {"name": "Tennents",
            "price": 2 
            },
            {"name": "whisky",
            "price": 4 
            }
        ]

    def test_pub_has_name(self): 
        self.assertEqual("The Clansman", self.pub.name)
        
    def test_add_drink(self):
        self.pub.add_drink(self.drinks)
        self.assertEqual

    
    # def test_find_drink_by_name(self):
    #     drink = self.pub.find_drink_by_name("whisky")
    #     self.assertEqual("whisky", drink["name"])

    def test_increase_total_cash(self): 
        self.pub.increase_total_cash(self.drinks[0]["price"])
        self.assertEqual(202.00, self.pub.total_cash)


def test_sell_drink_to_customer(self):
        self.assertEqual(2.50, self.customer.remove_customer_cash)
        self.assertEqual(204.00, self.test_increase_total_cash)

def test_check_customer_age(self):
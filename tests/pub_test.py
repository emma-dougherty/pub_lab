import unittest
from src.pub import Pub
from src.customer import Customer




class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jack Jarvis", 6.50, 76, 0)
        self.customer2 = Customer("Methedone Mick", 2.50, 17, 8)
        self.pub = Pub("The Clansman", 200.00)
        self.drinks = [
            {"name": "Tennents",
            "price": 2 ,
            "alcohol": 2
            },
            {"name": "whisky",
            "price": 4 ,
            "alcohol": 2
            }
        ]
        self.pub.add_drink( {"name": "Tennents", "price": 2, "alcohol": 2})
        self.pub.add_drink(  {"name": "whisky", "price": 4, "alcohol": 2})

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

    # def test_check_customer_age(self, customer):
    #     is_over_18 = self.pub.check_customer_age(customer)
    #     self.assertEqual(True, is_over_18)


    def test_sell_drink_to_customer(self):
        self.customer.buy_drink( self.drinks[0], self.pub )
        self.assertEqual(4.50, self.customer.purse)
        self.assertEqual(202.00, self.pub.total_cash)



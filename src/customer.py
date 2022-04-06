class Customer:
    def __init__(self, input_name, input_purse, input_age, input_drunkenness):
        self.name = input_name
        self.purse = input_purse
        self.age = input_age
        self.drunkenness = input_drunkenness

    def get_customer_cash(self):
        return self.purse
        
    def remove_customer_cash(self, amount):
        amount == self.drinks("price")
        self.purse -= amount
        return self.purse
    
    def get_drunkenness(self, drink):
        drink == self.drink.alcohol_level   
        self.drunkenness += self.drink.alcohol_level

    # def buy_drink(self, drink, pub):
    def buy_drink(self, drink):
        self.purse -= drink.price

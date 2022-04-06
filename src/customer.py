class Customer:
    def __init__(self, input_name, input_purse, input_age):
        self.name = input_name
        self.purse = input_purse
        self.age = input_age

    def get_customer_cash(self):
        return self.purse
        
    def remove_customer_cash(self, amount):
        self.purse -= amount
        return self.purse

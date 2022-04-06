class Pub:
    def __init__(self, input_name, input_total_cash):
        self.name = input_name
        self.total_cash = input_total_cash
        self.drinks = []

    
    def get_total_cash(self):
        return self.total_cash
    
    def increase_total_cash(self, amount):
        self.total_cash += amount
    
    # def find_drink_by_name(self, drink):
    #     for drink_name in self.drinks:
    #         if drink_name["name"] == drink:
    #             return drink_name

    def add_drink(self, drink):
        drink == self.drinks
        self.drinks.append(drink)

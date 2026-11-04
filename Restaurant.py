class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f'The restaurant serves "{self.restaurant_name}" and {self.cuisine_type.title()} cuisine.number of '
              f'tables served - {self.number_served}')
    def set_number_served(self,served_table):
        self.number_served += served_table
        print(f'number of people served - {self.number_served}')
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['Vanilla', 'Mint Chocolate Chip', 'Cookies and Cream', 'Salted Caramel']
    def list_flavors(self):
        print(f'We have varieties of ice cream:')
        for flavor in self.flavors:
            print(f'- {flavor}')
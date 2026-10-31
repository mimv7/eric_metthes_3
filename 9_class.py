# 9.1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'{self.cuisine_type.title()} is served at "{self.restaurant_name.title()}".')
    def open_restaurant(self):
        print('The restaurant is open now.')

restaurant = Restaurant('vkusnie sushi','Japanese food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9.2
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        desc = f'{self.cuisine_type.title()} is served at "{self.restaurant_name.title()}".'
        return desc
    def open_restaurant(self):
        text_opening_restaurant = 'The restaurant is open now.'
        return  text_opening_restaurant
    def general_information(self):
        print(self.describe_restaurant(),'\n',self.open_restaurant())

delicious_sushi = Restaurant('vkusnyye sushi','Japanese food')
eurasia = Restaurant('Eurasia','European and Asian cuisine')
chito_gvrito = Restaurant('Čito-Gvrito','Georgian cuisine')

delicious_sushi.general_information()
eurasia.general_information()
chito_gvrito.general_information()

# 9.3
class User:
    def __init__(self,first_name,last_name,registered_user = True):
        self.first_name = first_name
        self.last_name = last_name
        self.registered_user = registered_user
    def describe_user(self):
        return  f'Name:{self.first_name.title()}\nSurname:{self.last_name.title()}'
    def greet_user(self):
        if self.registered_user == True:
            print(f'{self.describe_user()}\n'
                'Welcome to the system')
        else:print(f'{self.describe_user()}\n'
                'You are not registered in the system.')

im = User('roman','meleshin')
im.greet_user()
hacker = User('user','user',registered_user=False)
hacker.greet_user()
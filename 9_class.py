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

# 9.4
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0      # обслужено столиков
    def describe_restaurant(self):
        print(f'{self.cuisine_type.title()} is served at "{self.restaurant_name.title()}".')
    def set_number_served(self,serviced_tables):
        self.number_served = serviced_tables       # заданное количество обслуженных столиков
        return self.number_served
    def increment_number_served(self,increased_number_tables):  # добавление обслуженных столиков
        self.number_served += increased_number_tables
        return self.number_served
    def info_restaurant(self):
        print(self.number_served)

restaurant = Restaurant('vkusnie sushi','Japanese food') #
restaurant.describe_restaurant()
restaurant.set_number_served(2)
restaurant.increment_number_served(2)
restaurant.info_restaurant()

# 9.5
class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def describe_user(self):
        full_name = f'Hello, {self.first_name.title()} {self.last_name.title()}!'
        print(full_name)
    def increment_login_attempts(self):
        self.login_attempts +=1
        return  self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts
    def info_login_attempts(self):
        print(f'Total number of login attempts - {self.login_attempts}')

my_user = User('roman','meleshin')
my_user.describe_user()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.info_login_attempts()
my_user.reset_login_attempts()
my_user.info_login_attempts()

# пример наследования
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'"{self.restaurant_name.title()}" serves {self.cuisine_type}.')


# В скобках указываем родителя, у которого воруем функционал
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        # super() говорит: "Эй, родитель, запусти свой __init__ и запиши имя и кухню"
        super().__init__(restaurant_name, cuisine_type)

        # А это уже личная, уникальная фишка потомка:
        self.flavors = ['Ванильное', 'Шоколадное', 'Клубничное']

    # Уникальный метод потомка, которого НЕТ у обычного ресторана
    def display_flavors(self):
        print("У нас в наличии следующие вкусы:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Создаем именно кафе-мороженое
my_ice_shop = IceCreamStand("Пломбирная Радость")

# 1. Потомок БЕЗ проблем вызывает метод родителя, хотя мы его внутри IceCreamStand не писали!
my_ice_shop.describe_restaurant()
# Выведет: "Пломбирная Радость" serves Ice Cream.

# 2. Потомок вызывает свой собственный уникальный метод
my_ice_shop.display_flavors()
# Выведет список вкусов

# 9.5
class Parent:
    def __init__(self,arg_1,arg_2):
        self.arg_1=arg_1
        self.arg_2=arg_2

class Dother(Parent):
    def __init__(self,arg_1,arg_2):
        super().__init__()
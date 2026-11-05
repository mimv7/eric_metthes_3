# =====================================================================
# 1. ОПРЕДЕЛЕНИЕ КЛАССОВ (Чертежи для будущих объектов)
# =====================================================================

class Battery:
    """КЛАСС: Описывает, как устроен аккумулятор."""

    def __init__(self, battery_size=40):
        """МЕТОД (Функция класса): Конструктор аккумулятора.

        Параметры:
          self — указывает на конкретный создаваемый аккумулятор.
          battery_size — числовое значение (по умолчанию 40).
        """
        # АТРИБУТ (Переменная объекта): Хранит размер батареи
        self.battery_size = battery_size

    def describe_battery(self):
        """МЕТОД (Функция класса): Выводит информацию на экран.

        Использует self, чтобы прочитать атрибут конкретного объекта.
        """
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar:
    """КЛАСС: Описывает, как устроен электромобиль."""

    def __init__(self, make, model, year):
        """МЕТОД (Функция класса): Конструктор электромобиля.

        Принимает текстовые и числовые параметры для описания машины.
        """
        # СТАНДАРТНЫЕ АТРИБУТЫ (Переменные объекта): Текст и числа
        self.make = make
        self.model = model
        self.year = year

        # СЛОЖНЫЙ АТРИБУТ (Экземпляр другого класса как атрибут):
        # Вызов Battery() создает реальный объект аккумулятора
        # и сохраняет его в атрибут self.battery нашей машины.
        self.battery = Battery()

    def get_descriptive_name(self):
        """МЕТОД (Функция класса): Собирает красивое название машины."""
        return f"{self.year} {self.make} {self.model}".title()


# =====================================================================
# 2. РАБОТА С КОДОМ (Создание и использование реальных объектов)
# =====================================================================

# ПЕРЕМЕННАЯ И ЭКЗЕМПЛЯР (Объект):
# my_leaf — это переменная.
# ElectricCar('nissan', 'leaf', 2024) — это создание реального объекта (экземпляра) по чертежу класса.
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# ВЫЗОВ МЕТОДА МАШИНЫ:
# Обращаемся к объекту машины и просим его выполнить свою функцию.
print(my_leaf.get_descriptive_name())

# ЦЕПОЧКА ВЫЗОВА (Сквозная точка):
# my_leaf — объект-машина.
# .battery — объект-аккумулятор, который лежит внутри этой машины.
# .describe_battery() — метод (функция), которая выполняется внутри аккумулятора.
my_leaf.battery.describe_battery()



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

# 9.6
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



kfc= Restaurant('kfc','american')
kfc.describe_restaurant()
kfc.set_number_served(5)
kfc.set_number_served(5)

ice_cream_truck = IceCreamStand('max','ice cream')
ice_cream_truck.describe_restaurant()
ice_cream_truck.list_flavors()

# 9.7
class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}')

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = ['post message','delete users','ban users']
    def show_privileges(self):
        print('Admin make:')
        for possibilities in self.privileges:
            print(f'- {possibilities}')

im_simple_user=User('roman','meleshin')
im_simple_user.greet_user()

admin_user = Admin('admin','pass')
admin_user.greet_user()
admin_user.show_privileges()

# 9.8
class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}')

class Privileges:
    def __init__(self):
        self.privileges = ['post message', 'delete users', 'ban users']
    def show_privileges(self):
        print('Admin make:')
        for possibilities in self.privileges:
            print(f'- {possibilities}')

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.possibilities = Privileges()


im_simple_user=User('roman','meleshin')
im_simple_user.greet_user()

admin_user = Admin('admin','pass')
admin_user.greet_user()
admin_user.possibilities.show_privileges()

# 9.9
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_desc_car(self):
        print(f'"{self.make.title()} {self.model}" {self.year}')

class Battery:
    def __init__(self,battery_capacity = 40):
        self.battery_capacity = battery_capacity
    def get_battery_capacity(self):
        print(self.battery_capacity)
    def upgrade_battery(self):
        if self.battery_capacity == 40:
            self.battery_capacity = 65

class ElectricCar(Car):
    def __init__(self, make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()


father_in_law_car=Car('niva','legend','2026')
father_in_law_car.get_desc_car()

my_car= ElectricCar('ferrari','luce','2026')
my_car.get_desc_car()
my_car.battery.get_battery_capacity()
my_car.battery.upgrade_battery()
my_car.battery.get_battery_capacity()

# 9.10
from Restaurant import Restaurant
burger_king = Restaurant('burger king','american')
burger_king.describe_restaurant()
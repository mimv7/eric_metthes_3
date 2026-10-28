# 9.1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):                      #class method
        print(f'The restaurant "{self.restaurant_name.title()}" offers {self.cuisine_type}.')
    def open_restaurant(self):                          #class method
        print('The restaurant is open now.')

delicious_sushi = Restaurant('vkusnyye sushi','Japanese food') #class instance
nuovo_Vesuvio = Restaurant('Nuovo Vesuvio','Italian food')
pkhali_Khinkali = Restaurant('ПхалиХинкали','Georgian cuisine')

delicious_sushi.describe_restaurant()                    #method call
nuovo_Vesuvio.describe_restaurant()
pkhali_Khinkali.describe_restaurant()

# 9.3
class User:
    """class User"""
    def __init__(self,firs_name,last_name):
        self.firs_name =  firs_name
        self.last_name =  last_name
    def describe_user(self):
        name = f'{self.firs_name.title()} {self.last_name.title()}'
        return name
    def greet_user(self):
        print(f'Greetings, {self.describe_user()}.')

im_user = User('roman','meleshin')
im_user.greet_user()
# 8.12
def gathering_ingredients(spread,*ingridients, base = 'bread'):
    # получение и вывод состава бутерброда
    print(f'\nBase of a sandwich - {base}:')
    print(f'\tA spread for a sandwich - {spread}')
    for num, ingredient in enumerate(ingridients, start=1):
        print(f'\t{num} ingredient - {ingredient}')

gathering_ingredients('butter')
gathering_ingredients('rama','lard', 'offal', 'pig ears')

# 8.13
def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('roman', 'meleshin',
                             location='Saint-Petersburg',
                             field='QA engineer')
print(user_profile)

# 8.14
def show_car_info(manufacturer,model,color='blue',tow_package =True, **car_info):
    # показать информацию о машине
    car_info['manufacturer']=manufacturer
    car_info['model']=model
    print(car_info)


show_car_info('bmw','m5',class_car='sport')
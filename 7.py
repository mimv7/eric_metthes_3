# 7.1
car = input('Tell me, what make of car would you like?: ')
print(f'Let\'s see if I can find a {car.upper()} for you.')

# 7.2
guests = input('How many guests are expected? ')
guests = int(guests)
if guests <9:
    print('You can book a table now.')
elif guests > 8:
    print('You\'ll have to wait a little while.')
else:
    print('you did something wrong')

# 7.3
num = int(input('Enter a number: '))
if num%10 == 0:
    print('This number is a multiple of ten.')
else:
    print('this number')

# 7.4
while True:
    pizza_topping = input('Name a topping you would like to add: ')
    if pizza_topping == 'q':
        print('Topping addition complete.')
        break
    print(f'Your {pizza_topping} has been added to the pizza.')

# 7.5
while True:
    visitor_sage = int(input('Enter the visitor\'s age: '))
    if visitor_sage < 3:
        print('Free admission')
    elif 3<= visitor_sage < 12:
        print('The ticket costs 10 dollars.')
    elif visitor_sage >= 12:
        print('The ticket costs 15 dollars.')
    else:
        print('error')
    if visitor_sage == 'q':
        break

# 7.8
current_sandwich = ['tuna', 'chicken', 'cheese', 'big mak', 'vegetarian', ]
finished_sandwiches = []
while current_sandwich:
    item_sandwich = current_sandwich.pop(0)
    finished_sandwiches.append(item_sandwich)
for ingredient in finished_sandwiches:
    print(f'I created a {ingredient} sandwich')

# 7.9
current_sandwich = ['breakfast','breakfast','tuna', 'chicken', 'cheese', 'big mak', 'vegetarian','breakfast' ]
print('Breakfast is sold until 10:00 a.m.')
while 'breakfast' in current_sandwich:
    current_sandwich.remove('breakfast')
for ingredient in current_sandwich:
    print(f'I created a {ingredient} sandwich')

# 7.10
survey = True
survey_result = {}
print(survey_result)
while survey:
    question = input('Let\'s start the survey. If not, then click "n"')
    if question.lower() == 'n':
        survey = False
        print('The survey is finished.')
        break

    user = input('What is your name: ')
    vacation_destination = input('If you could visit one place in the world, where would you go? ')
    survey_result[user] = vacation_destination
print("--- Survey Results ---")
for name,place in survey_result.items():
    print(f'{name.title()} wanted to go to {place.title()}.')

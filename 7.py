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
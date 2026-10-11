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
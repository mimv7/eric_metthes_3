# 5.3
alien_color_ver1 = 'red'
alien_color_ver2 = 'green'
if alien_color_ver1 == 'green':
    player_points_ver1 = 5
elif alien_color_ver1 == 'red':
    player_points_ver1 = 0
else:
    print('error')
print(player_points_ver1)
# 5.4
alien_color = 'red'
if alien_color == 'green':
    player_points = 5
else:
    player_points = 10
print(player_points)

# 5.6
age = 41
if age < 2:
    print('baby')
elif 2 <= age < 4:
    print('Baby')
elif 4 <= age < 13:
    print('child')
elif 13 <= age < 20:
    print('teenager')
elif 20 <= age < 65:
    print('adult')
elif 65 <= age:
    print('elderly')
else:
    print('error')

# 5.7
favorites_fruits = ['banana','strawberry','cherry']
magazine_fruits = ['banana', 'kiwi','watermelon']
for fruit in favorites_fruits:
    if fruit in magazine_fruits:
        print(f'I love {fruit}!')

# 5.8
users = ['sveta','roman','MAMA','admin','papa']
for user in users:
    if user.lower() == 'admin':
        print(f'Hello, {user.title()}! Would you like to view the status report?')
    else:
        print(f'Hi, {user.title()}! Thanks for logging into the system.')

# 5.9
users = ['sveta','roman','MAMA','admin','papa']
if users:
    for user in users:
        if user.lower() == 'admin':
            print(f'Hello, {user.title()}! Would you like to view the status report?')
        else:
            print(f'Hi, {user.title()}! Thanks for logging into the system.')
else:
    print('No users')

print('\n'*3)
users = []
if users:
    for user in users:
        if user.lower() == 'admin':
            print(f'Hello, {user.title()}! Would you like to view the status report?')
        else:
            print(f'Hi, {user.title()}! Thanks for logging into the system.')
else:
    print(f'\tNo users')

# 5.10
current_users = ['sveta','roman','MAMA','admin','papa',]
current_users_lower = [user_lower.lower() for user_lower in current_users]
new_users = ['sveta','roman','MAMA','admin','Vladimir','joe','papa',]
for user in new_users:
    if user.lower() in current_users_lower:
        print(f'Hello, {user.title()}, this name is already in use. Please choose a new username.')
    else:
        print(f'Hello, {user.title()}!')

#5.11
ordinal_numbers = []
nums = list(range(1,10))
for num in nums:
    if num == 1:
        ordinal_numbers.append(f'{num}st')
    elif num == 2:
        ordinal_numbers.append(f'{num}nd')
    elif num == 3:
        ordinal_numbers.append(f'{num}rd')
    else:
        ordinal_numbers.append(f'{num}th')
for ordinal_number in ordinal_numbers:
    print(ordinal_number)

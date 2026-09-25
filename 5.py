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
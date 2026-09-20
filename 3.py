# 3.1
names = ['roman','sveta','mama']
print(names[0].title())
print(names[1].title())
print(names[2])

# 3.3
guitars =['cort', 'ibanez','yamaha']
print(f'I would like to by {guitars[0].title()}!')
print(f'I would like to by {guitars[1].title()}!')
print(f'I would like to by {guitars[2].title()}!')

# 3.4
guests = ['roma','sveta','mama','papa']
print(f'{guests[0].title()}, invite you to the party!')
print(f'{guests[1].title()}, invite you to the party!')
print(f'{guests[2].title()}, invite you to the party!')
print(f'{guests[3].title()}, invite you to the party!')

# 3.5
guests[3] = 'andrei'
print(guests)
print(f'{guests[0].title()}, invite you to the party!')
print(f'{guests[1].title()}, invite you to the party!')
print(f'{guests[2].title()}, invite you to the party!')
print(f'{guests[3].title()}, invite you to the party!')
guests.insert(0,'genek')
guests.insert(3,'noname')
guests.append('victor')
print(guests)
del_guests = guests.pop(3)
print(guests)
print(f'{del_guests}, who are you?')
del guests[0]
del guests[-1]
del guests[-1]
del guests[-1]
print(guests)

# 4.1
pizzas = ['4 cheeses', 'margarita', 'dodo']
for pizza in pizzas:
    print(f'I love pizza {pizza.title()}')
print('\ti love so match pizza')

# 4.3
for num in range(1,21):
    print(num)

# 4.4
hundred_num = list(range(1,101))
print(hundred_num)
print(min(hundred_num))
print(max(hundred_num))
print(sum(hundred_num))

# 4.6
odd_mum = list(range(1,21,2))
print(odd_mum)

# 4.7
three = list(range(3,31,3))
print(three)

# 4.8
cubes = [num ** 3 for num in range(1,11)]
print(cubes)

# 4.10
alf = ['a','b','c','d','e','f','g','h']
print(alf[:3])
print(alf[1:4])
print(alf[-3:])

# 4.11
friends_pizzas = pizzas[:]
friends_pizzas.append('pineapple')
print('my favorite pizzas:')
for pizza in pizzas:
    print(f'\t{pizza}')
print('friends favorite pizzas:')
for pizza in friends_pizzas:
    print(f'\t{pizza}')
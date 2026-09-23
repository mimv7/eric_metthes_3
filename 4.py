# 4.1
pizzas = ['4 cheeses', 'margarita', 'dodo']
for pizza in pizzas:
    print(f'I love pizza {pizza.title()}')
print('\ti love so match pizza')

# 4.3
for num in range(1,21):
    print(num)

# 4.4
thousand_num = list(range(1,1_001))
print(thousand_num)
print(min(thousand_num))
print(max(thousand_num))
print(sum(thousand_num))

# 4.6
odd_mum = list(range(1,21,2))
print(odd_mum)

# 4.7
three = list(range(3,31,3))
print(three)

# 4.8
cubes = [num ** 3 for num in range(1,11)]
print(cubes)

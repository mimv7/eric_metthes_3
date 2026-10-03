# 6.1
im = {
    'first_name': 'Roman',
    'last_name':'Meleshin',
    'age':41,
    'city':'Saint-Petersburg',
}
print(im['first_name'])
print(im['last_name'])
print(im['age'])
print(im['city'])

for value in im.values():
    print(f'\t{value}')

# 6.2
favorite_numbers ={
    'roman': 7,
    'sveta': 3,
    'mama': 13,
}
for k,v in favorite_numbers.items():
    print(f'{k}: {v}')

# 6.3
glossary = {
    'string': 'Серия символов, которая обрабатывается как текст.',
    'list': 'Коллекция элементов, расположенных в определенном порядке.',
    'dictionary': 'Коллекция пар "ключ-значение", связывающая данные.',
    'loop': 'Блок кода, который повторяется, пока выполняется условие.',
    'variable': 'Именованованное место в памяти для хранения данных.',
}
for k,v in glossary.items():
    print(f'{k}:\n\t{v}')
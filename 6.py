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

# 6.5
rivers ={
    'nile':'egypt',
    'amazonka':'america',
    'neva':'russia',
}
for k,v in rivers.items():
    print(f'{k.title()} flows through the {v.title()}.')

# 6.6
favorite_languages = {
    'roman':'python',
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phill':'python',
}
respondents = ['roman','sveta','jen','sarah','mama','papa','jenny','python']
for respondent in respondents:
    if respondent.lower() in favorite_languages:
        print(f'Thank you, {respondent.title()}, for participating in the survey.')

    else:
        print(f'{respondent.title()}, tell me, what is your favorite programming language?')

# 6.7
numbers = []
num = 5
for i in range(10):
    print(i)

    numbers.append(num)
    num += 5
print(numbers[0:5])
print(numbers)


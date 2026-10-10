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
people = {
    'im' : {
        'first_name': 'Roman',
        'last_name':'Meleshin',
        'age':41,
        'city':'Saint-Petersburg',
    },
    'sveta':{
        'first_name': 'Sveta',
        'last_name':'Meleshina',
        'age':38,
        'city':'Saint-Petersburg',
    },
    'mama':{
            'first_name': 'marina',
            'last_name':'Meleshina',
            'age':63,
            'city':'Kaluga',
        }
}
for login, info_login in people.items():
    full_name = f'{info_login['first_name'].title()} {info_login['last_name'].title()}'
    print(login)
    print(f'\t{full_name}')
    print(f'\t{info_login['age']}')
    print(f'\t{info_login['city']}')

# 6.8
favorite_places = {
    'im':['Palace Square','Nevsky Prospekt','300th Anniversary Park'],
    'sveta':['Furshtatskaya Street','Kirov Park','Murinsky Park'],
    'mama':['Dvortsy village','forest','Ugra River'],
}
for name, places in favorite_places.items():
    print(name.title())
    for place in places:
        print(f'\t{place}')

# 6.11
cities ={
    'Санкт-Петербург':{
        'country':'Russia',
        'population':5_600_000,
        'fact':'Изначально Петербург строился на 42 островах.'
               ' Сейчас в городе насчитывается более 340 мостов (из которых около 20 — разводные). Суммарная длина всех водотоков и каналов города превышает 280 километров.'
    },
    'Калуга':{
            'country':'Russia',
            'population':325_000,
            'fact':'Колыбель космонавтики: Это официальное прозвище и главный бренд города. Именно здесь большую часть жизни жил и работал выдающийся ученый Константин Циолковский, заложивший теоретические основы космонавтики. В Калуге открыт уникальный Государственный музей истории космонавтики имени К. Э. Циолковского — первый в мире и крупнейший в России, первый камень в фундамент которого заложил лично Юрий Гагарин.'
        },
    'Лос-анджелес':{
                'country':'USA',
                'population':3_860_000,
                'fact':'Лоскутное одеяло без центра: Лос-Анджелес уникален своей урбанистической структурой. В отличие от большинства мировых столиц, у него практически нет единого исторического или культурного центра. Мегаполис выглядит как гигантское лоскутное одеяло, сшитое из 88 самостоятельных городов (таких как Беверли-Хиллз, Санта-Моника, Лонг-Бич и Малибу), каждый из которых имеет своего мэра и полицию.'
            }
}
for city, info in cities.items():
    print(f'{city}:')
    print(f'\tCountry: {info['country']}')
    print(f'\tPopulation: {info['population']}')
    print(f'\tFact: {info['fact']}')
    print()
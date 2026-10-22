# 8.1
def display_message():
    print('You are going through the eighth chapter, which is called "Function."')
display_message()

# 8.2
name_book = 'Eric Matthes: Learning Python'
def favorite_book(title):
    print(f'One of my favorite books is "{title}"')

favorite_book(name_book)

# 8.2
def make_shirt(size,inscription):
    print(f'Your T-shirt size is {size}, and it says "{inscription}" on it.')

make_shirt(56,'Python')
make_shirt(size=56,inscription='Python')

# 8.3
def make_shirt_2(size='L',inscription='i love Python'):
    print(f'Your T-shirt size is {size}, and it says "{inscription}" on it.')

make_shirt_2()
make_shirt_2(46,'i love jS')

# 8.4
def describe_city(city,country='Russia'):
    print(f'{city.title()} is in {country.title()}.')

describe_city('moscow')
describe_city('Saint-Petersburg')
describe_city('maima','usa')

# 8.6
def city_country(city,country):
    the_countrys_capital =f'{city.title()}, {country.title()}!'
    return  the_countrys_capital
print(city_country('Moscow','Russia'))
print(city_country('Washington','usa'))
print(city_country('novograd','ordania'))

# 8.7
def make_album(performer,album_title,songs_album=''):
    album = {'performer':performer,
             'album_title':album_title,}
    if songs_album:
        album['sougs']=songs_album
    return  album

print(make_album('Король и Шут','Жаль, нет ружья'))
print(make_album('Linkin Park','Hybrid Theor',12))
print(make_album(' AC/DC','Highway to Hell'))

# 8.8
def make_album(performer, album_title, songs_album=''):
    """Строит словарь с информацией о музыкальном альбоме."""
    album = {
        'performer': performer,
        'album_title': album_title,
    }
    if songs_album:
        album['songs'] = songs_album
    return album


# Запускаем бесконечный цикл, как требует задание
while True:
    print("\nВведите информацию об альбоме.")
    print("(введите 'q' в любой момент для выхода)")

    in_performer = input("Исполнитель: ")
    if in_performer.lower() == 'q':
        break

    in_album_title = input("Название альбома: ")
    if in_album_title.lower() == 'q':
        break

    in_songs = input("Количество треков (необязательно): ")
    if in_songs.lower() == 'q':
        break

    # Обрабатываем количество треков, если они были введены
    if in_songs:
        in_songs = int(in_songs)
    else:
        in_songs = ''

    # Создаем альбом и выводим его на экран внутри цикла
    in_album = make_album(in_performer, in_album_title, in_songs)
    print(f"\nСоздан словарь: {in_album}")

# 8.9
def show_message(messages):
    for message in messages:
        print(f'\n\t {message}')

# Простой список текстов сообщений
message_for_the_Python_course = [
        "Привет! 👋 Завтра покажем, как написать первый скрипт на Python за 10 минут. Будет только практика!",
        "А вы знали, что Python-код в 3 раза короче Java? Собрали топ-3 сферы для старта новичка: [ссылка]",
        "Ловите обещанный чек-лист: 'Пошаговый план перехода в IT с нуля' 🎁 [ссылка]",
        "🔥 Места на интенсив по Python заканчиваются. Старт в понедельник. Успейте записаться: [ссылка]"
]
show_message(message_for_the_Python_course)

# 8.10
def send_message(massages,sent_messages):
    while massages:
        phrase = massages.pop()
        sent_messages.append(phrase)
    print(sent_messages)
    print(massages)

sent_messages =[]

send_message(message_for_the_Python_course[:],sent_messages)
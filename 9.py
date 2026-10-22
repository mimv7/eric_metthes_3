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


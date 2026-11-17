# 10.1
from pathlib import Path

file = Path("file_txt/learning_python.txt")
message = file.read_text()
print(message * 2)

# 10.2
text_replace = file.read_text()
text_replace = text_replace.replace("Python", "C++")
print(text_replace)

# 10.3
file = Path("file_txt/pi_digitals.txt")
message = file.read_text()
for line in message.splitlines():
    print(line)

# 10.4
# name = input('input name:')
# file = Path('file_txt/name.txt')
# write_name = file.write_text(name.title())

# 10.5
# path = Path('file_txt/name.txt')
# list_name = ''
# while True:
#     name = input('name:')
#     if name == 'q':
#         break
#     list_name += name + '\n'
# names = path.write_text(list_name)

# 10.6
# try:
#     num_1 = int(input('num 1: '))
#     num_2 = int(input('num 2: '))
# except ValueError:
#     print('enter a number')
# else:
#     summ = num_1 + num_2
#     print(summ)

# 10.7
# while True:
#     try:
#         num_1 = input('num 1: ')
#         if num_1 =='q':
#             break
#         num_2 = input('num 2: ')
#         if num_2 == 'q':
#             break
#         summ = (int(num_1)+ int(num_2))
#     except ValueError:
#         print('enter a number')
#     else:
#         print(summ)

# 10.8
locating_files = ["file_txt/cats.txt", "file_txt/dogs.txt", "file_txt/dog.txt"]
for i in locating_files:
    file = Path(i)
    try:
        content = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("File not found")
    else:
        print(content)

# 10.9
locating_files = ["file_txt/cats.txt", "file_txt/dogs.txt", "file_txt/dog.txt"]
for i in locating_files:
    file = Path(i)
    try:
        content = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(content)

# 10.10
url_loc_file = "file_txt/dracula.txt"
file = Path(url_loc_file)
content = file.read_text(encoding="utf-8")
#print(content)
print(content.lower().count("row"))

# 10.11
import  json
from pathlib import Path

from pathlib import Path
import json

# # 1. Получаем число от пользователя
# favorite_num = int(input('Enter your favorite number: '))
#
# # 2. Указываем адрес файла (сам файл на диске пока не создан)
# file = Path('file_json/numbers.json')
#
# # 3. Упаковываем число Python в текстовый формат JSON
# content = json.dumps(favorite_num)
#
# # 4. Создаём файл по указанному пути и записываем туда строку JSON
# file.write_text(content)
#
# # 5. Читаем сырой текст из файла обратно в программу
# you_num = file.read_text()
#
# # 6. Распаковываем текст JSON обратно в настоящее число Python
# favorite_num = json.loads(you_num)
#
# # 7. Выводим результат
# print(favorite_num)

# 10.12
file = Path('file_json/numbers.json') # путь до файла
if file.exists():
    print('true')
    you_num = file.read_text()
    try:
        favorite_num = json.loads(you_num)
        print(f'Your favorite number is {favorite_num}')
    except json.JSONDecodeError:
        print('base is failed')
        number = int(input('The database might be broken, so please enter a new number: '))
        content = json.dumps(number)
        file.write_text(content)


    #print(favorite_num)
else:
    number = int(input('Enter your favorite number: '))
    content = json.dumps(number)
    file.write_text(content)

# 10.13
from pathlib import Path
import json

users ={}
name = input('give your name: ')
surname = input('enter your surname: ')
login = input('enter your login: ')
path = Path('file_json/users.json')
def new_user(name,surname,login):
    users['name'] = name
    users['surname'] = surname
    users['login'] = login
    for k,v in users.items():
        user =  f'{k} - "{v}"'
        return user


content = json.dumps(users) # Convert the contents of a variable into a JSON file
apdated_user = path.write_text(content) # I am writing a JSON file
print('user data:')
print(user)

new_user(name,surname, login)

# 10.14

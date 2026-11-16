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

# favorite_num = int(input('Enter your favorite number: '))
# file = Path('file_json/numbers.json') # путь до файла
# content = json.dumps(favorite_num) # загрузить содержимое в формат
# number = file.write_text(content) # записать в путь файла
#
# you_num = file.read_text() # прочитать из пути содержимое
# favorite_num = json.loads(you_num) # загрузить из содержимого
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
# 10.1
from pathlib import Path

file = Path('file_txt/learning_python.txt')
message = file.read_text()
print(message*2)

# 10.2
text_replace=file.read_text()
text_replace = text_replace.replace('Python','C++')
print(text_replace)

# 10.3
file = Path('file_txt/pi_digitals.txt')
message = file.read_text()
for line in message.splitlines():
    print(line)

# 10.4
# name = input('input name:')
# file = Path('file_txt/name.txt')
# write_name = file.write_text(name.title())

# 10.5
path = Path('file_txt/name.txt')
list_name = ''
while True:
    name = input('name:')
    names = path.write_text(name)
    list_name+=names
    if name=='q':
        break

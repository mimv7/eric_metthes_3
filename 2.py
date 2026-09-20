# 2.1
print('hello, Python, world!')

# 2.2
message = 'hello'
print(message)
message = 'Hi!'
print(message)

# 2.2/1
url = 'https://stepik.org/lesson/1166614/step/7?unit=1178936'
no_starch_url = url.removeprefix('https://')
print(no_starch_url)

# 2.3
name = 'roman'
message = f'Hi, {name.title()}, do learn Python today?'
print(message)

# 2.4
name = 'sveta'
print(name.lower())
print(name.upper())
print(name.title())

# 2.5
print('Альберт Эйнштейн однажды сказал: "Тот, кто никогда не совершал ошибок, никогда не пробовал ничего нового".')

# 2.6
EINSTEIN_NAME = 'Альберт Эйнштейн'
massage = 'Тот, кто никогда не совершал ошибок, никогда не пробовал ничего нового'
print(f'{EINSTEIN_NAME} однажды сказал: "{massage}"')

# 2.8
file = 'python_notes.txt'
file_name = file.removesuffix('.txt')
print(file_name)

# 2.9
print(5+3)
print(10-2)
print(4*2)
print(int(32/4)) # !!! else 8.0

# 2.10
favorite_num = 7
print(f'My favorite number - {favorite_num}')

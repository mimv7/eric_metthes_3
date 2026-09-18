# 2.1
from selenium import webdriver

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

driver = webdriver.Chrome()
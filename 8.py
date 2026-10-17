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
describe_city('kaluga')

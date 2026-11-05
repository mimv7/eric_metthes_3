from User import User
class Privileges:
    def __init__(self):
        self.privileges = ['post message', 'delete users', 'ban users']
    def show_privileges(self):
        print('Admin make:')
        for possibilities in self.privileges:
            print(f'- {possibilities}')

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.possibilities = Privileges()
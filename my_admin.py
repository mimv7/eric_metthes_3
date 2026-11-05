from User import User
from Admin import Admin
my_admin = User('admin','admin')
my_admin.greet_user()
my_admin_2=Admin('sys','admin')
my_admin_2.greet_user()
my_admin_2.possibilities.show_privileges()
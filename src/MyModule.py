# import custom class (as module) that we created before
# and use it
from MyClasses import MyAge

my_age = MyAge("1996-04-18", "Steve")
print(my_age.show_me_my_age())
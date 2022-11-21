# import custom class (as module) that we created before
# and use it
from my_classes import MyAge

guddu = MyAge("1985-01-01", "Shri Guddu")
guddu.show_me_my_age()
print(guddu._MyAge__my_name)
print( f"{guddu.show_me_my_age()}")
# > 'Mr James, you are so young, only 41 years old!'

# additional learexample with the import as command

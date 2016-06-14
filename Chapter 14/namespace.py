import newton

# A namespace is another way to define a scope. When an object is defined within a namespace it is like defining it within a function. Any definition within a namespace is considered local to that namespace.
def square(number):
   print("not from the newton module")
   return number * number

num = 12
print("Square from newton.py: ")
print(newton.square(num)) # qualified by namespace
print("Square from main program: ")
print(square(num)) # same square function but qualified by local program instead

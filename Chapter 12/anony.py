#anonymous function
#lambda form

#def square(number):
#   return number * number

square = lambda x: x*x
print(square(2))
numbers = [1,2,3,4]
numberssq = list(map(lambda x:x*x, numbers)) # saves the trouble of having to define the function separately - it is defined anonymously right within the argument
print(numberssq)

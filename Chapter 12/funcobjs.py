def square(number):
   return number * number

num = 2
sqnum = square(num)
sqnumber = square # a function is object just like any other in Python and can be assigned to a variable
sqnum = sqnumber(2)
print(sqnum)

#map higher-order function
numbers = [1,2,3,4]
numberssq = list(map(square, numbers)) # passing a function as an argument to another function
print(numberssq)

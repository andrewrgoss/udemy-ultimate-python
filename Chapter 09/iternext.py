# numbers = [1,2,3]
# it = iter(numbers)
# #print(next(it))
# #print(next(it))
# #print(next(it))
fileIt = open('grades.txt', 'r') # when a file is opened an iterator is automatically called, so no need for the iter function here
print(next(fileIt),)
print(next(fileIt),)

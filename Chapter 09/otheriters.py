#numbers = range(1,11)
#it = iter(numbers)
#print(next(it))
import os
files = os.popen('dir *.py') # popen runs os command for current directory and returns specified data in an object that is iterable
fileit = iter(files)
print(next(fileit), end='')
print(next(fileit), end='')
print(next(fileit), end='')
print(next(fileit), end='')

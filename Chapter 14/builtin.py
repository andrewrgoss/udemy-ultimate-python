import os
import math

files = os.popen("dir *.py") # works with current working directory by default
for file in files:
   print(file, end='')

print(math.fabs(-123.45))

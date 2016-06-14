# scope
# global / local

def getNumber():
   print(number)

# main (or global area), outside a class or function
number = 1 # any other part of the program can access the value of this variable, since it is global in scope
print(number)
getNumber()

import math

def hypotenuse(s1, s2):
   def square(num): # nested function has access to variables of the outer function (hypotenuse)
      return num * num
   return math.sqrt(square(s1) + square(s2))

print("Enter the length of side 1: ")
side1 = int(input())
print("Enter the length of side 2: ")
side2 = int(input())
hyp = hypotenuse(side1, side2)
print("The hypotenuse is " + str(hyp))

#5! = 5 * 4 * 3 * 2 * 1
#5! = 5 * 4!
def fact(number):
   if number <= 1:
      return 1
   else:
      return number * fact(number-1) # function calls itself (recursion)

print(fact(10))

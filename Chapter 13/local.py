def square(number):
   squared = number * number # squared is a local variable bc it is defined w/in the body of the function square
   return squared

print(square(2))
print("Squared (defined in square function): " + str(squared)) # squared is not defined globally, so this will produce an error

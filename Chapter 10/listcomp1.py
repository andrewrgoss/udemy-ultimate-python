# Intro to List Comprehensions
# grades = [71, 81, 77, 84]
# print(grades)
# for i in range(len(grades)):
#   grades[i] = grades[i] + 5
# grades = [grade + 5 for grade in grades]
# print(grades)
words = ['NOW','IS','THE','TIME']
print(words)
words = [word.lower() for word in words] # backward for loop written as one single expression as part of one single statement
print(words)

# outFile = open('text.txt', 'w')
# outFile.write('this is line 1\n')
# outFile.write('this is line 2\n')
# outFile.close()
outFile = open('grades.txt', 'w') # 'w' argument opens the file for writing
grade = 0
print("Enter a grade (q to quit): ")
grade = raw_input()
while (grade != 'q'):
   outFile.write(grade + '\n')
   print("Enter a grade (q to quit): ")
   grade = raw_input()

outFile.close()

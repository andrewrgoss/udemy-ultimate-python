# N = range(1,101)
# EN = [x for x in N if x % 2 == 0]
# print(EN)
sent = "now is the time for all good people to come to the aid "
sent += "of their party"
print(sent)
words = sent.split() # creates a list of string elements
wlen = [(word, len(word)) for word in words]
for i in wlen:
   print(i)

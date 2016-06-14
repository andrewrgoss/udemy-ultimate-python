numer = 0
denom = 0
while denom != -1:
    print("Enter a numerator: ")
    numer = float(raw_input())
    print("Enter a denominator: ")
    denom = float(raw_input())
    if denom == 0:
       continue # returns program back to beginning of while loop (ln 4) before calling the print statement below (ln 10)
    print(numer / denom)

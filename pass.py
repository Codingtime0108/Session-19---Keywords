b = int(input("Enter a number more than 5:"))
for a in range(b):
    if a%3 == 0:
        print("buzz")
    elif a%5 == 0:
        print("fizz")
    elif a%15 == 0:
        pass
    elif a%20 == 0:
        print("twist")
    else:
        print (a)   
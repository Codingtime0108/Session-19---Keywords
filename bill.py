#Write a program to calculate the customer due amount after paying a bill of a certain amount so 100 note but total = 90 so output 10
a = int(input("Enter bill amount: "))
b = int(input("Enter due amount: "))

if b>a:
    print("this is too high take",b-a,"back")
else:
    print("This was your change",b-a)
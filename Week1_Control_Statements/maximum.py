"""wap to input three numbers and print the maximum among them"""

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if a>=b and a>=c:
    print("the max num is a")
elif b>=a and b>=c:
    print("the max num is b")
else:
    print("the max num is c")
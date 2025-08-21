""" read N, print no. of digits in N."""

N = int(input("enter the number"))
digit = 0
while N>0:
    N = N//10
    digit+=1
print(digit)
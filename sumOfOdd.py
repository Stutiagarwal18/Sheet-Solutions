""" Take an integer A as input. You have to print the sum of all odd numbers in the range [1, 
A]. """

A= int(input("enter the number:"))
i= 1
sum =0
while i<=A:
    sum +=i
    i +=2
print(sum)
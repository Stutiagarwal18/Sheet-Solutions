""" You are given an integer A, you need to find and return the sum of all the even numbers 
between 1 and A. Even numbers are those numbers that are divisible by 2. """

A= int(input("enter the number:"))
i= 2
sum =0
while i<=A:
    sum +=i
    i +=2
print(sum)
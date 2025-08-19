""" Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as 
input from user """

N= int(input("enter the number:"))
i= 1
sum =0
while i<=N:
    sum +=i
    i +=1
print(sum)
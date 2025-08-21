""" read N, print sum of digits in N."""

N= int(input("enter the number:"))
sum =0
while N>0:
    sum += N%10
    N = N// 10
print(sum)

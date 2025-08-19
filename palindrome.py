
"""palindrome"""

A = int(input("Enter a number: "))
original = A
rev = 0

while A > 0:
    digit = A % 10
    rev = rev * 10 + digit
    A = A // 10

if rev == original:
    print("Yes")
else:
    print("No")

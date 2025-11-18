A = input()
A = A + A
B = ""

for ch in A:
    if not ('A' <= ch <= 'Z'):
        B = B + ch

for v in "aeiou":
    B = B.replace(v, "#")

print(B)
"""Given two lists A1 and A2, each containing integers, write a Python program to compute
 the element-wise sum of the corresponding elements in the two lists and store the result
 in a new list."""

A1 = [1, 2, 3, 4]
A2 = [4, 5, 6, 7]
result = []
for i in range(len(A1)):
    result.append(A1[i] + A2[i])
print(result)

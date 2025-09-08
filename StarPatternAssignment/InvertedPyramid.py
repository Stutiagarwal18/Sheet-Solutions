# * * * * * * * * * 
# * * * * * * *
# * * * * *
# * * *
# *

n = 5
for i in range(n, 0, -1):
    for j in range(2*n-1):
        if j < 2*i-1:   # star condition
            print("*", end=" ")
        else:
            print(" ", end="")
    print()

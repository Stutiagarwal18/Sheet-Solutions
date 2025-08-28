n= int(input("enter no. of rows"))
for i in range(1,n+1):
    print("*",end=" ")
    for j in range(n+1-i):
        print("_",end=" ")
    print("*",end =" ")
    print()
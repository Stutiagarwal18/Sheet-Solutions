"""you are given 3 integer angles of a triangle. tell whether the triangle is valid or not."""

a = int(input("enter first angle"))
b= int(input("enter second angle"))
c = int(input("enter third angle"))

if a>0 and b>0 and c>0 and (a+b+c == 180):
    print("it is a triangle")
else:
    print("not valid")
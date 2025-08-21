"""accept the percentage from the user and display the grade according to criteria """

percentage = int(input("enter the percentage"))

if percentage>=90 and percentage<100:
    print("grade O")
elif percentage>=80 and percentage<90:
    print("grade A")
elif percentage>=70 and percentage<80:
    print("grade B")
elif percentage>=60 and percentage<70:
    print("grade c")
else:
    print("Fail")
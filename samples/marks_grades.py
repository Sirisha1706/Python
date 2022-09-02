# grades beased on marks
num=int(input("Enter the marks?"))
if num>=80:
    print("Your grade 'A'")
elif num in range(70,80):
    print("Your grade 'B'")
elif num in range(50,70):
    print("Your grade 'C'")
else:
    print("Your grade 'D'")
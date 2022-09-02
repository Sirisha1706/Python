
student = {}
while True:
    name = input("enter name?")
    if name == "end":
        break
    marks = int(input("enter marks?"))
    if name in student:
        student[name]+= marks
    else:
        student[name]= marks

for k, v in student.items():
    print(f"{k:10} {v}")
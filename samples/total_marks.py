marks = ['1,78', '2,67', '2,76', '3,89', '1,98', '3,87']
students={}
for m in marks:
    rollno, value=m.split(',')
    if rollno in students:
        students[rollno]=students[rollno]+int(value)
    else :
        students[rollno]=int(value)
for rollno,total in sorted(students.items()):
    print(f"{rollno:5} {total:5}")
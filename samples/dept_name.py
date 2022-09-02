employ = {}
f = open("dept_names.txt","rt")
for line in sorted(f.readlines()):
    value = line.split(",")
    dept_no = value[0].strip()
    names = value[1].strip()
    if dept_no in employ:
            employ[dept_no].add(names)
    else:
         employ[dept_no] = {names}
f.close()
for dept_no,names in sorted(employ.items()):
    print(f"{dept_no:5} {','.join(names)}")
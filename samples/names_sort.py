# accept names until end and sort them
names = set()
while True:
    nam = input("enter names(end to stop)")
    if nam == "end":
        break
    names.add(nam)
for m in sorted(names):
    print(m)
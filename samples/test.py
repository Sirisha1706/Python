marks = {}
na = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in marks:
        marks[score].add(name)
    else:
        marks[score] = {name}
for s,n in sorted(marks.items()):
    print(f"{' '.join(n)}")
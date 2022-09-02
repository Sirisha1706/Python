# take user and display its words
s = input("Enter string:")
w = 1
for i in s[::]:
    if i == " ":
        w += 1
    else:
        continue

print(w)
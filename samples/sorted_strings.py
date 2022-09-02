words=[]
while True:
    word = input("enter words['end' to end]?")
    if word == 'end':

        break
    words.append(word)
for w in sorted(words):
    print(w)

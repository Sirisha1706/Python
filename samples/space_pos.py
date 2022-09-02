sen = input("enter the sentence?")
pos=-1
while True:
    pos = sen.find('', pos+1)
    if pos != -1:
        break
    print(pos)

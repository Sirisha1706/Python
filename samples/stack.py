data=[]
while True:
    print("1.push\n2.pop\n3.display\n4.exit")
    choice=int(input("enter choice?[0-4]"))
    if choice == 4:
        break
    if choice==1:
        value=int(input("enter value?"))
        data.append(value)
    elif  choice==2:
        print("pop value=", data.pop())
    else :
        print(data)

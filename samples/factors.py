# factors of a number
num=int(input("Enter the number?"))
for i in range(2,num//2+1):
    if num%i==0:
        print(i)
else:
    print("Prime Number")

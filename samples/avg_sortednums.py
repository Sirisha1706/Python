# take 10 nums and sort them
num=[]
sum = 0
for i in range(10):
    n = int(input("Enter  numbers?"))
    num.append(n)
for n in num:
    sum = sum + n
print(sum/len(num))

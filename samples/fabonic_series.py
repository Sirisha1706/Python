n = int(input("Enter no of terms?"))
a=0
b=1
print(a,b, end=' ')
for _ in range(n):
    x = a+b
    print(x, end=' ')
    a=b
    b=x

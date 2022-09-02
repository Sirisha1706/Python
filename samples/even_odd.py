# even or odd number
n = int(input("Enter the number?"))
even = odd = 0
for i in range(1, n):
    if i % 2 == 0:
        even = even+i
    else:
        odd = odd+i
print(even, odd)
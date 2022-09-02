num = n = int(input("Enter number?"))
f = 0
while n > 0:
    d = n % 10
    f += d**3
    n = n//10

if f == num:
    print(num, " is a Armstrong number")


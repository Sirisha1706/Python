# LCM and GCD of numbers
a=int(input("Enter number?"))
b=int(input("Enter number?"))
# GCD
num=a if a<b else b
for i in range(num,0,-1):
    if a%i==0 and b%i==0:
        gcd=i
        print(f"GCD={i}")
        break
# LCM
print(f"LCM={(a*b)/gcd}")
def even_odd(n):
    return 0 if n %2 == 0 else 1

nums=[]
while True:
   num = int(input("enter the nums?[0 to end]"))
   if num == 0:
       break
   nums.append(num)
for n in sorted(nums, key=even_odd):
    print(n)

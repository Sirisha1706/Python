# displaying all the numbers greater than average
nums = []
while True:
    num = int(input("enter the numbers?[0 to end]"))
    if num == 0:
      break
    nums.append(num)
avg = sum(nums)// len(nums)

for n in nums:
    if n >= avg:
        print(n)



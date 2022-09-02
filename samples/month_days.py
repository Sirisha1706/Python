# no of days based on month(excluding leap years)
month=int(input("Enter the month(1-12):"))
if month in [1,3,5,7,8,10,12]:
    print("31 days")
elif month == 2:
    print("28 days")
else :
    print("30 days")
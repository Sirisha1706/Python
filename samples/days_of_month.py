# days of month including leap year
month=int(input("Enter the month(1-12):"))
if month in [1,3,5,7,8,10,12]:
    print("31 days")
elif month == 2:
    yr=int(input("Enter year?"))
    if yr%4==0 and yr%100!=0 or yr%400==0:
        print("29 days")
    else :
        print("28 days")
else :
    print("30 days")
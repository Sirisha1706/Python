import re
import math


def distance(n: list):
    x2 = y2 = s = 0
    for j in n:
        x, y = j
        x1 = ord(x)
        y1 = int(y)
        if x2 != 0 and y2 != 0:
            d = ((x1-x2)**2)+((y1-y2)**2)
            s = s + math.sqrt(d)
        x2 = x1
        y2 = y1
    return s


a = input('Enter the coordinates(X-Y)(X:(A-Z)and Y:(1-26)) of points?(separate by comma)')
c = a.split(",")
o = []
for i in c:
    b = re.compile('([A-Z])([0-9]+)')
    p = b.match(i).groups()
    o.append(p)
path = distance(o)
print(path)

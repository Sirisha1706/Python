
customer = {}
while True:
    name = input("enter name?")
    if name == "end":
        break
    mobile = input("enter mobile?")
    if name in customer:
        customer[name].add(mobile)
    else:
        customer[name]= {mobile}

for k, v in customer.items():
    print(f"{k:10} {','.join(v)}")
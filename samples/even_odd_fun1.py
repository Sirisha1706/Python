def even_odd(numbers:list):
    odd = 0
    for n in numbers:
        if n%2==0:
            odd+=1
    return (len(numbers)-odd, odd)

print(even_odd([34, 56, 67, 53, 87, 12, 43]))
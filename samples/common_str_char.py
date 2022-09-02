# common characters b/w strings
st1 = "sirisha"
st2 = "sundari"
for ch in set(st1):
    for c in set(st1):
        if ch == c:
            print(ch)
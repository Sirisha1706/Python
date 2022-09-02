# frequency of character occuring in a string
str = "hello! I am sirisha sundari sadhu"
ch = []
for ch in set(str):
    print(f"{ch} occure {str.count(ch)}")

# frequency of words in string
st = " Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked "
wd = st.split()
for w in set(wd):
    print(f"{w} occure {st.count(w)}")
    
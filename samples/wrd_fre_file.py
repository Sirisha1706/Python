with open(r"d:\sirisha\Python\text_doc\old_man.txt", 'rt') as f:
        con = f.read()
        con = con.replace("\n", ' ')
        wd = con.split(" ")
        for w in sorted(set(wd)):
            w = w.strip()
            print(f"{w:20}  {con.count(w)}")


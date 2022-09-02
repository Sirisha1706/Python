import re
with open(r"d:\sirisha\Python\text_doc\old_man.txt", encoding='utf-8') as f:
        con = f.read()
        con = con.replace("\n", ' ')
        wd = re.findall(r"[A-Za-z0-9'_]+", con)
        for w in sorted(set(wd)):
            print(f"{w:20}  {con.count(w)}")


from re import fullmatch

pattern1 = r"\s*\w{12,}\s*"
pattern2 = r"[^ieaou]+"
pattern3 = r"^[^ieaou]\w+[^ieaou]$"
pattern4 = r"^[ieaou]\w+[ieaou]$"
pattern5 = r"^\w{3}$"

for i in range(5, 21, 2):
    pattern = r"^\w{" + str(i) + "}$"
    pattern5 = pattern5 + "|" + pattern

print(pattern5)

with open("dictionary-tur.txt", mode="r") as myfile:
    for word in myfile.readlines():
        word = word.strip()
        if fullmatch(pattern5, word):
            print(word)

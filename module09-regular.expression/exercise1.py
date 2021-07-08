# Regular Expression -> template -> Language ("1234-1234-1234-1234")
# "1234-123-12345-123" ? Credit Card
# File -> Search e-mail
# 1) . + * () {} [] ? \w \W \s \S \d \D ... -> template
# 2) Python: import re, fullmatch, sub, split, search, ...

meyveler = ["elma", "armut", "kiraz", "kavun", "karpuz", "kivi", "ananas", "seftali", "muz"]

pattern1 = r"^k.*z$"  # k ile başlayacak z ile bitecek
pattern2 = r"[a-zA-Z]{1,4}"  # en fazla dört karakterli
pattern3 = r"[a-zA-Z]{5,}"  # en beş karakterli
pattern4 = r"\w{5,}"  # en beş karakterli
pattern5 = r".*[ai].*"
pattern6 = r"[^ai]*"
pattern7 = r".*ar.*"
pattern8 = r"[0-9]{11}"
pattern9 = r"\d{11}"
empty_line_pattern = r"^\s*$"

fulltext="""This is the first line.                 
         This is the second line.
   This is the last line.                          
"""

from re import fullmatch

for meyve in meyveler:
    if fullmatch(pattern7, meyve):
        print(meyve)

if fullmatch(pattern8, "1234567a891"):
    print("This is a valid identity no!")
else:
    print("This is NOT a valid identity no!")

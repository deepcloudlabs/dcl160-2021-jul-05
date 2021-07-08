from re import fullmatch, split
from turtledemo.chaos import line

empty_line_pattern = r"^\s*$"
empty_line_count = 0
line_count = 0
word_count = 0
char_count_wows = 0
char_count = 0

with open("war-and-peace.txt", mode="r") as myfile:
    for line in myfile.readlines():
        line_count += 1
        if fullmatch(empty_line_pattern, line):
            empty_line_count += 1
        words = split(r"\s+", line)
        word_count += len(words)
        char_count += len(line)
        for word in words:
            char_count_wows += len(word)

print(f"Empty line: {empty_line_count}")
print(f"Line Count: {line_count}")
print(f"Fullness: {(100 * (line_count - empty_line_count)) / line_count}")
print(f"Words: {word_count}")
print(f"Characters (with spaces): {char_count}")
print(f"Characters (w/o spaces): {char_count_wows}")

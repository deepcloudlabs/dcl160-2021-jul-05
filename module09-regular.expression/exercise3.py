from re import fullmatch
from turtledemo.chaos import line

empty_line_pattern = r"^\s*$"
empty_line_count = 0
line_count = 0

with open("war-and-peace.txt", mode="r") as myfile:
    for word in myfile.readlines():
        line_count += 1
        if fullmatch(empty_line_pattern, word):
            empty_line_count += 1

print(empty_line_count, line_count, (100 * (line_count-empty_line_count)) / line_count)

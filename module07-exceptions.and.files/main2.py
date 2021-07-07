employees = [
    ("jack shephard", "Sales", 100000, 1978, True),
    ("kate austen", "IT", 200000, 1985, False),
    ("ben linus", "Finance", 150000, 1967, True),
    ("james sawyer", "HR", 70000, 1979, True),
    ("kim kwon", "Sales", 120000, 1986, True),
    ("sun kwon", "IT", 170000, 1984, False),
    ("hugo reyes", "IT", 120000, 1992, True)
]

try:
    myfile = open("employees2.txt", mode="w")
    for full_name, department, salary, birth_year, full_time in employees:
        myfile.write(f"{full_name},{salary},{birth_year},{department},"
                     f"{'FULL_TIME' if full_time else 'PART_TIME'}\n")  # text i/o
    print("Employees are saved to the file")
except FileNotFoundError as err:
    print(err)
finally:
    myfile.close()

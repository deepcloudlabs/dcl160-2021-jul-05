employees = []
with open("employees.txt", mode="r") as myfile:
    for line in myfile:
        employee = line.strip().split(",")
        full_name, salary, birth_year, department, full_time = employee
        employees.append((full_name, float(salary), int(birth_year),
                          department, full_time == "FULL_TIME"))
    print(employees)

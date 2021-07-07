with open("employees.txt", mode="r") as myfile:
    employees = [(full_name, float(salary), int(birth_year), department, full_time == "FULL_TIME")
                 for full_name, salary, birth_year, department, full_time in
                 [line.strip().split(",") for line in myfile]]
for employee in employees:
    print(employee)

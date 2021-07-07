import json
from _ast import expr

with open("employees.json", mode="r") as json_file:
    employees_data = json.load(json_file)
    for employeee in employees_data["employees"]:
        print(employeee)


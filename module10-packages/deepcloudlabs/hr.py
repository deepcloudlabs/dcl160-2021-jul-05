class Employee:
    def __init__(self, fullname, email, salary):
        self.fullname = fullname
        self.email = email
        self.salary = salary

    def __str__(self):
        return f"employee (full name: {self.fullname})"

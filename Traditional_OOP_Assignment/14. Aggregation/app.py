# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id


class Department:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees or []  
    
    def add_employee(self, employee):
        self.employees.append(employee)

emp1 = Employee("Helen", 555)  
dept = Department("HR")        
dept.add_employee(emp1)        

print(f"Department: {dept.name}, Employee: {dept.employees[0].name}, ID: {dept.employees[0].emp_id}")





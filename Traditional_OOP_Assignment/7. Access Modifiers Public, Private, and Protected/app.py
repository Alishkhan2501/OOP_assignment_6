# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

emp = Employee("Ali", 20000, "012$%^&895")

print(emp.name)       # ✅ Works (Public)
print(emp._salary)    # ⚠️ Works, but not recommended (Protected)
print(emp.__ssn)      # ❌ Error (Private)


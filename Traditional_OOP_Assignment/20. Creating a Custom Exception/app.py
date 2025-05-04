# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...exception

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 25:
        raise InvalidAgeError("Age must be 25 or older")
    return "Valid age"
try:
    check_age(20)
except InvalidAgeError as e:
    print(f"Error: {e}")  
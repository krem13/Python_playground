print("Starting the program...")

try:
    #4/0
    #print(name)
    print("Inside try block...")
except NameError:
    print("Error: Variable 'name' is not defined.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception:
    print("Error: An unexpected error occurred.")

def upper_case_name(name):
    if not name:
        raise ValueError("Name cannot be empty")
    return name.upper()

#print(upper_case_name(""))

print(int(9))

print("after error handling...")
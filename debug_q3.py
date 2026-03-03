name = input("Name: ")
age = int(input("Age: "))  # FIX 1: Convert string to int

if age >= 18:  # FIX 2: Now comparison works
    status = "Adult"
else:
    status = "Minor"

# FIX 3: Correct f-string formatting
print(f"{name} is {age} years old and is a {status}")

# FIX 4: Now age is int, so addition works
print(f"In 5 years: {age + 5}")

score = 85.5
print(f"Score: {score:.0f}")  # FIX 5: Correct format specifier
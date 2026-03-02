# 1. Ask the user for their name
name = input("What is your name? ")

# 2. Ask for their birth year
birth_year = input("What year were you born? ")

# 3. Calculate their age (Current year is 2026)
age = 2026 - int(birth_year)

# 4. Print the result
print(f"Hi {name}! You are (or will be) {age} years old this year.")
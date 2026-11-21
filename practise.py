print("User Defined Function Examples\n")

# Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Saksham", 20)


# Default Arguments
def info(country="India"):
    print(f"I am from {country}.")

info("Japan")
info()


# Keyword Arguments
def student_info(name, course):
    print(f"Student Name: {name}, Course: {course}")

student_info(course="B.Tech CSE", name="Saksham")


# Variable Length Arguments (*args)
def add_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    print("Sum is:", total)

add_numbers(5, 10, 15, 20)


# Variable Length Keyword Arguments (**kwargs)
def display_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_details(Name="Saksham", Age=20, Course="B.Tech CSE")

print("---------- Lambda Function Examples ----------")

# Example 1: Convert string to uppercase
s1 = 'Python Programming'
s2 = lambda func: func.upper()
print(s2(s1))

# Example 2: Check Positive, Negative or Zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-1))
print(n(0))

# Example 3: Lambda addition
add = lambda x, y: x + y
print(f"Lambda addition: {add(5, 3)}")

# Example 4: Square numbers using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(f"Squared numbers (using lambda with map): {squared_numbers}")

# Example 5: Filter even numbers using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (using lambda with filter): {even_numbers}")


print("\n---------- List Comprehension Examples ----------")

# Example 1: Create a list of fruits containing 'a'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(f"Fruits containing 'a': {newlist}")

# Example 2: Double the numbers in a list
numbers = [1, 2, 3, 4]
doubled_numbers = [num * 2 for num in numbers]
print(f"Doubled numbers: {doubled_numbers}")

# Example 3: Square numbers using list comprehension
squared_list_comp = [x * x for x in numbers]
print(f"Squared numbers (using list comprehension): {squared_list_comp}")

# Example 4: List of even numbers from 1 to 10
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(f"Even numbers from 1 to 10: {even_numbers}")

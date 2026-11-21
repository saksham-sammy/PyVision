import math
import random

print("---------- MATH MODULE ----------")

# Example 1: Logarithm
n = 25
print("log base 10 value is:", math.log10(n))
a = 16
b = 2
log_a_base_b = math.log(a) / math.log(b)
print("log base 2 of 16 (using change of base):", log_a_base_b)
num = 5 ** 3
log_num_base_5 = math.log(num, 5)
print("log base 5 of 125:", log_num_base_5)

# Example 2: Trigonometric functions
print("\nsin(30 degrees):", math.sin(math.radians(30)))
print("cos(60 degrees):", math.cos(math.radians(60)))
print("tan(45 degrees):", math.tan(math.radians(45)))

# Example 3: Ceil and Floor
value = 3.2
floor_value = 4.8
print("\nCeiling of", value, "is", math.ceil(value))
print("Floor value of", floor_value, "is", math.floor(floor_value))

# Example 4: Constants
print("\nThe value of Pi is:", math.pi)
print("The value of e is:", math.e)

print("\n---------- RANDOM MODULE ----------")

# Example 1: Random integer
number = random.randint(1, 10)
print("\nRandom integer between 1 and 10:", number)

# Example 2: Random choice
fruits = ['apple', 'banana', 'mango', 'grapes']
choice = random.choice(fruits)
print("Random fruit selected:", choice)

# Example 3: Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

# Example 4: Dice Roll Game
print("\n Welcome to the Dice Roll Game!")
input("Press Enter to roll the dice...")
dice = random.randint(1, 6)
print("You rolled a", dice)

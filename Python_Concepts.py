# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M8npkdFpiHt0lKRgySIMBVBHvwFKtkEy
"""

print("Hello, World!")

"""Variables, Operations and Data Types"""

# Variables and basic operations
a = 5
b = 3
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)

# Variables and Data Types
number = 10  # Integer
floating_point = 3.14  # Float
text = "Hello, World!"  # String
is_true = True  # Boolean

# Checking data types
print(type(number))
print(type(floating_point))
print(type(text))
print(type(is_true))

"""Control Structures"""

# If...Else Statements
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

"""Loops"""

# For loop
for i in range(5):
    print(i)

# While loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

"""Conditional Statements"""

# Conditional Statements
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

"""Functions"""

# Functions
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

"""Lists and Dictionaries"""

# Lists
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # Accessing the first element
fruits.append("grape")  # Adding an element
print(fruits)

# Dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Accessing value by key

"""Classes and Objects"""

# Classes and Objects
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

car = Car("Toyota", "Corolla")
car.display_info()

"""Exception Handling"""

# Exception Handling
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error:", e)

"""File Handling:"""

# File Handling - Writing to a file
with open("example.txt", "w") as file:
    file.write("This is an example text.")

# File Handling - Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

"""Modules and Libraries"""

# Modules and Libraries
import math

print(math.sqrt(25))

"""List Comprehensions"""

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

"""Lambda Functions"""

# Lambda Functions
square = lambda x: x * x
print(square(5))

"""Object-Oriented Programming Concepts"""

# Inheritance
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

"""Slicing"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Splitting into two parts
split_index = 5
first_part = my_list[:split_index]
second_part = my_list[split_index:]

print("First part:", first_part)
print("Second part:", second_part)

my_string = "apple,orange,banana,grape"
fruits_list = my_string.split(',')
print(fruits_list)

"""String Operations"""

# String Concatenation (Merging)
string1 = "Hello, "
string2 = "World!"
merged_string = string1 + string2
print(merged_string)

# String Splitting
sentence = "This is a sample sentence."
words = sentence.split()  # Splitting by spaces (default)
print(words)

# Splitting with a specific delimiter
csv_data = "apple,orange,banana,grape"
fruits = csv_data.split(',')
print(fruits)

# String Substring
text = "Hello, World!"
substring = text[7:]  # Extracting substring
print(substring)

# Changing Case
text_upper = text.upper()
text_lower = text.lower()
print(text_upper)
print(text_lower)

# String Joining
words_list = ["This", "is", "a", "sentence"]
sentence = ' '.join(words_list)  # Joining with a space
print(sentence)

# String Formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

"""Merging"""

# Merging Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using the + operator
merged_list = list1 + list2
print(merged_list)

# Using the extend() method
list1.extend(list2)
print(list1)

# Merging Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1.copy()  # Make a copy to preserve original dict1
merged_dict.update(dict2)
print(merged_dict)

# Merging Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

merged_set = set1.union(set2)
print(merged_set)

# Using the | operator
merged_set_operator = set1 | set2
print(merged_set_operator)

# Merging Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2
print(merged_tuple)

"""Generators"""

# Generator
def square_numbers(nums):
    for num in nums:
        yield num * num

my_nums = square_numbers([1, 2, 3, 4, 5])
for num in my_nums:
    print(num)

"""Decorators"""

# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

"""Map, Filter, and Reduce"""

# Map, Filter, Reduce
# map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce() - (In Python 3, moved to functools module)
from functools import reduce
product = reduce((lambda x, y: x * y), numbers)
print(product)
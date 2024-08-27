#!/usr/bin/env python
# coding: utf-8

# # 1. Function Basics
# 
# 

# In[16]:


def subtract(a, b):
    """This function subtracts b from a and returns the result."""
    return a - b

# Example usage
result = subtract(10, 3)
print(f"Subtracting 3 from 10 gives: {result}")


# # 2. Addition with Condition 

# In[17]:


def addition(a, b):
    """This function adds or subtracts two numbers based on their values."""
    if a > b:
        result = a + b
    else:
        result = a - b
    return result

# Example usage
result = addition(7, 5)
print(f"Addition result based on condition: {result}")


# # 3. Using Lambda Functions

# In[18]:


add = lambda a, b: a + b

# Example usage
result = add(4, 6)
print(f"Using lambda, adding 4 and 6 gives: {result}")


# # 4. Filtering Even Numbers from a List

# In[19]:


def filter_even(numbers):
    """This function filters out even numbers from a list."""
    return list(filter(lambda x: x % 2 == 0, numbers))

# Example usage
numbers = [1, 2, 3, 4, 1, 2, 6, 5, 7, 2, 4, 9]
even_numbers = filter_even(numbers)
print(f"Even numbers filtered from the list: {even_numbers}")


# # 5. Mapping with Lambda

# In[20]:


def double_numbers(numbers):
    """This function doubles the value of each number in the list."""
    return list(map(lambda x: x * 2, numbers))

# Example usage
numbers = [1, 2, 3, 4]
doubled = double_numbers(numbers)
print(f"Doubled numbers from the list: {doubled}")


# # 6. Counting Uppercase and Lowercase Letters

# In[21]:


def count_case(s):
    """This function counts the number of uppercase and lowercase letters in a string."""
    counts = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for char in s:
        if char.isupper():
            counts["UPPER_CASE"] += 1
        elif char.islower():
            counts["LOWER_CASE"] += 1
    return counts

# Example usage
sentence = "Hello World!"
case_count = count_case(sentence)
print(f"Uppercase letters: {case_count['UPPER_CASE']}, Lowercase letters: {case_count['LOWER_CASE']}")


# # 7. Multiplication of Numbers in a List

# In[22]:


def multiply(numbers):
    """This function multiplies all the numbers in a list."""
    total = 1
    for num in numbers:
        total *= num
    return total

# Example usage
numbers = [2, 3, 4]
product = multiply(numbers)
print(f"Product of numbers in the list: {product}")


# # 8. Unique Elements from a List

# In[23]:


def unique_list(lst):
    """This function returns a list of unique elements."""
    unique = []
    for elem in lst:
        if elem not in unique:
            unique.append(elem)
    return unique

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = unique_list(numbers)
print(f"Unique elements from the list: {unique_numbers}")


# # 9. Pangram Checker

# In[24]:


def is_pangram(s):
    """This function checks if the given string is a pangram."""
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
pangram_status = is_pangram(sentence)
print(f"Is the sentence a pangram? {'Yes' if pangram_status else 'No'}")


# # 10. Using a Dictionary

# In[25]:


dic = {"Iron": "Man", "Captain": "Marvel"}

# Example usage
for key in dic:
    print(f"{key}: {dic[key]}")


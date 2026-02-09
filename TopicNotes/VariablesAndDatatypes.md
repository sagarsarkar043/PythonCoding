#  Variables, Data Types, Type Casting & Comments in Python

---

## 1. Variables in Python

### What is a Variable?
A **variable** is a name that stores data in memory.  
Python is **dynamically typed**, meaning you don’t need to declare the data type explicitly.

### Variable Assignment

```python
x = 10
name = "Alice"
price = 99.99
Rules for Naming Variables
✔ Must start with a letter or underscore (_)
✔ Can contain letters, numbers, underscores
❌ Cannot start with a number
❌ Cannot use Python keywords

valid_name = 10
_valid = 20
total_sales_2024 = 5000
Invalid Variable Names
2value = 10      # ❌ Cannot start with number
total-sales = 5 # ❌ Hyphen not allowed
class = 3       # ❌ Keyword
2. Python Data Types (Core)
Python has several built-in data types.
The four most important for analytics are:

int

float

string

boolean

3. Integer (int)
What is an Integer?
An integer is a whole number (positive, negative, or zero).

count = 10
temperature = -5
year = 2025
Integer Operations
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a // b)  # Integer division
print(a % b)   # Modulus
4. Float
What is a Float?
A float represents decimal or fractional numbers.

price = 49.99
average_score = 87.5
discount = 0.15
Float Operations
x = 10.5
y = 2.5

print(x + y)
print(x * y)
print(x / y)
5. String (str)
What is a String?
A string is a sequence of characters enclosed in:

Single quotes ' '

Double quotes " "

name = "Sagar"
city = 'Mumbai'
String Operations
first_name = "Data"
last_name = "Analyst"

full_name = first_name + " " + last_name
print(full_name)
String Indexing & Slicing
text = "Python"

print(text[0])     # P
print(text[-1])    # n
print(text[0:4])   # Pyth
6. Boolean (bool)
What is Boolean?
Boolean represents True or False values.

is_active = True
is_completed = False
Boolean in Conditions
age = 20

is_adult = age >= 18
print(is_adult)  # True
Boolean with Logical Operators
x = 10
y = 5

print(x > 5 and y < 10)  # True
print(x < 5 or y < 10)   # True
7. Checking Data Types
Use the type() function to identify the data type.

x = 10
y = 10.5
z = "Python"
flag = True

print(type(x))
print(type(y))
print(type(z))
print(type(flag))
8. Type Casting (Type Conversion)
What is Type Casting?
Type casting is converting one data type into another.

Python provides built-in functions:

int()

float()

str()

bool()

Converting int to float
x = 10
y = float(x)

print(y)
print(type(y))
Converting float to int
price = 99.99
rounded_price = int(price)

print(rounded_price)  # 99
Converting string to int / float
quantity = "50"
price = "99.5"

q = int(quantity)
p = float(price)

print(q)
print(p)
⚠️ The string must contain valid numeric values.

Converting to string
total = 500
message = "Total Sales: " + str(total)

print(message)
Boolean Type Casting
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("Data")) # True
9. Comments in Python
Why Use Comments?
Comments are used to:

Explain code

Improve readability

Help others understand logic

Single-Line Comments
# This is a comment
sales = 500  # Assigning sales value
Multi-Line Comments / Docstrings
"""
This function calculates total sales
Used in monthly sales reporting
"""
10. Documentation Using Docstrings
Docstrings describe:

What a function does

Parameters

Return values

def calculate_total(price, quantity):
    """
    Calculates total cost

    Parameters:
    price (float): price of item
    quantity (int): number of items

    Returns:
    float: total cost
    """
    return price * quantity
11. Real-World Data Analytics Example
product = "Laptop"
price = 50000.50
quantity = 2
is_available = True

total_cost = price * quantity

print("Product:", product)
print("Total Cost:", total_cost)
print("Available:", is_available)
12. Common Mistakes to Avoid
❌ Using wrong type in calculations
❌ Forgetting type casting
❌ Using unclear variable names
❌ Ignoring comments and documentation

13. Key Takeaways
Variables store data

Python supports dynamic typing

int, float, string, boolean are core data types

Type casting is essential in analytics

Clean comments improve maintainability

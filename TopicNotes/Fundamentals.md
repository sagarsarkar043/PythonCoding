# Python Introduction, Syntax & Indentation  
*A Complete Foundation for Data Analytics*

---

## 1. Introduction to Python

### What is Python?
Python is a **high-level, interpreted, general-purpose programming language** created by **Guido van Rossum** and released in **1991**.

Python emphasizes:
- Code readability
- Simplicity
- Fewer lines of code
- Rapid development

Python code is close to **plain English**, making it ideal for beginners and professionals alike.

---

## 2. Why Python is Popular in Data Analytics

Python has become the **industry standard** for Data Analytics because:

- Easy to learn and write
- Powerful libraries for data handling
- Strong community support
- Works well with databases, Excel, and BI tools
- Extensively used in interviews and real-world projects

---

## 3. Usage of Python in Data Analytics Lifecycle

Python is used across the **entire analytics pipeline**.

### 1️. Data Ingestion
- Reading CSV, Excel, JSON files
- Connecting to databases
- Calling APIs

### 2️2. Data Cleaning
- Handling missing values
- Removing duplicates
- Standardizing data formats

### 3️. Data Analysis
- Aggregations
- Filtering
- Grouping
- Business metric calculation

### 4️. Data Visualization
- Trend analysis
- Distribution analysis
- KPI dashboards

### 5️. Automation
- Automated reports
- Scheduled scripts
- Data validation checks

---

## 4. Applications of Python

### Business & Analytics
- Sales analysis
- Customer segmentation
- Churn analysis
- Financial reporting
- KPI monitoring

### Technology
- Automation scripts
- Web development
- Machine learning models

### Industry Usage
- Banking & Finance
- Retail & E-commerce
- Healthcare
- Telecom
- Supply Chain & Logistics

---

## 5. Python Syntax – Core Characteristics

Python syntax is designed to be **clean, readable, and minimal**.

### Key Syntax Rules
- No semicolons (`;`) required
- No curly braces (`{ }`) for blocks
- Indentation defines code structure
- Case-sensitive language

Example:
```python
x = 10
y = 20
print(x + y)
```

## 6. Python Indentation (🔥 Extremely Important)

### What is Indentation?
Indentation refers to the **spaces at the beginning of a line of code**.

Python uses indentation to define:
- Code blocks
- Logical structure
- Execution scope

Unlike other programming languages, Python does **not** use `{}`.

---

### Correct Indentation Example

```python
if 10 > 5:
    print("10 is greater than 5")
    print("This line is inside the if block")
✔ Both lines belong to the if block.
```
### Incorrect Indentation Example
```
if 10 > 5:
print("10 is greater than 5")
```
❌ This will raise an IndentationError.

### Indentation Rules
-Use 4 spaces per indentation level

-Do not mix tabs and spaces

-All statements in a block must align properly

## 7. Indentation in Control Structures

### if–else Statement
```
age = 17

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
for Loop
for i in range(1, 6):
    print(i)
    print("Loop is running")
while Loop
count = 1

while count <= 3:
    print("Count:", count)
    count += 1
```
## Function Definition
```
def calculate_average(total, count):
    average = total / count
    return average
```    
## 8. Python Statements & Line Structure

### Single-Line Statement
x = 100

### Multiple Statements in One Line (Valid but Not Recommended)
x = 10; y = 20; z = x + y
Avoid this in analytics code for better readability.

### Multi-Line Statement Using Parentheses
total_sales = (1200 + 1500 +
               1800 + 2100)

## 9. Python Case Sensitivity
Python treats uppercase and lowercase letters differently.
```
value = 10
Value = 20

print(value)  # 10
print(Value)  # 20
```

## 10. Python Comments

### Single-Line Comments
This is a comment - '#'

sales = 500  # Assigning sales value

### Multi-Line Comments / Docstrings
"""
This block explains the purpose of the program
Used for documentation
"""

## 11. Python Keywords

Keywords are reserved words and cannot be used as variable names.

Examples
-if, else, for, while

-def, return

-import

-True, False, None
```
import keyword
print(keyword.kwlist)
```
## 12. Best Practices for Clean Python Code

✔ Use meaningful variable names
✔ Maintain consistent indentation
✔ Avoid unnecessary complexity
✔ Write readable and maintainable code

## 13. Real-World Data Analytics Example
```
sales = [1000, 1500, 1200, 1800]

total_sales = 0

for amount in sales:
    total_sales += amount

print("Total Sales:", total_sales)
```

## 14. Common Syntax & Indentation Errors
❌ Missing Colon

`
if sales > 1000
    print("High sales")
`	
❌ Mixed Tabs and Spaces

`
if sales > 1000:
	print("High sales")
    print("Check formatting")
`

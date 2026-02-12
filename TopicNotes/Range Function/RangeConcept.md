# range() in Python

## Introduction

The range() function in Python is used to generate a sequence of numbers.
It is most commonly used in loops (especially for loops).

## What is range()?

range() returns a range object, which represents an immutable sequence of numbers.It does NOT create a list directly (in Python 3).To see the numbers, you convert it to a list.
```
print(range(5))        # Output: range(0, 5)
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]
```

## Syntax of range()

There are 3 ways to use it:

### 1. range(stop)

range(stop)
- Starts from 0
- Ends at stop - 1
- Step = 1 (default)

Example:
```
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

### 2. range(start, stop)

range(start, stop)
-Starts from start
-Ends at stop - 1
-Step = 1

Example:
```
for i in range(2, 6):
    print(i)
```

Output:
```
2
3
4
5
```
### 3. range(start, stop, step)

range(start, stop, step)
-Starts from start
-Stops before stop
-Increments by step

Example:
```
for i in range(1, 10, 2):
    print(i)
```

Output:
```
1
3
5
7
9
```

## Important Rules

### Stop value is excluded

range(5) → 0 to 4
range(1, 5) → 1 to 4
This is called half-open interval.

### Step cannot be zero

range(1, 10, 0)  # ❌ Error
Error:
ValueError: range() arg 3 must not be zero

### Negative step (Reverse order)

```
for i in range(10, 0, -2):
    print(i)
```

Output:
```
10
8
6
4
2
```

### Converting range() to List

```
numbers = list(range(5))
print(numbers)
```

Output:
```
[0, 1, 2, 3, 4]
```
### Using range() with len()

Common in indexing lists:

```
fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])
```

Output:
```
0 apple
1 banana
2 mango
```

### Checking Membership

```
r = range(1, 10)
print(5 in r)   # True
print(15 in r)  # False
```

### Range Object Properties

```
r = range(2, 20, 3)
print(r.start)  # 2
print(r.stop)   # 20
print(r.step)   # 3
```

### Memory Efficiency

range() is memory efficient because it does not store all numbers.

```
r = range(1, 1000000000)
```

This does NOT consume huge memory.

### Practical Examples

#### Example 1: Sum of first N numbers

```
n = 5
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)
```

#### Example 2: Multiplication Table

```
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

#### Example 3: Even Numbers

```
for i in range(2, 21, 2):
    print(i)
```

### Common Mistakes

- Forgetting stop is excluded
- Using step = 0
   Wrong direction with negative step

Example of mistake:

```
range(1, 10, -1)  #  Nothing prints
```

Correct:

```
range(10, 1, -1)
```

### Advanced Usage

Reverse using reversed()

```
for i in reversed(range(5)):
    print(i)
```

Output:

```
4
3
2
1
0
```

Creating Custom Step Pattern

```
print(list(range(0, 50, 5)))
```

Output:
```
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
```

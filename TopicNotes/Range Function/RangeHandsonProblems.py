# =============================================
# Python range() Practice - 20 Problems
# Generated from Jupyter Notebook
# =============================================


# -------------------------------------------------
# 1. Print numbers from 0 to 9
# -------------------------------------------------

for i in range(10):
    print(i)


# -------------------------------------------------
# 2. Print numbers from 1 to 20
# -------------------------------------------------

for i in range(1, 21):
    print(i)


# -------------------------------------------------
# 3. Print even numbers from 1 to 20
# -------------------------------------------------

for i in range(2, 21, 2):
    print(i)


# -------------------------------------------------
# 4. Print odd numbers from 1 to 20
# -------------------------------------------------

for i in range(1, 21, 2):
    print(i)


# -------------------------------------------------
# 5. Print numbers from 10 to 1 (reverse)
# -------------------------------------------------

for i in range(10, 0, -1):
    print(i)


# -------------------------------------------------
# 6. Sum of first N natural numbers
# -------------------------------------------------

n = 5
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)


# -------------------------------------------------
# 7. Multiplication table of 7
# -------------------------------------------------

num = 7
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# -------------------------------------------------
# 8. Count numbers divisible by 3 between 1 and 50
# -------------------------------------------------

count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1
print("Count:", count)


# -------------------------------------------------
# 9. Print squares from 1 to 10
# -------------------------------------------------

for i in range(1, 11):
    print(i * i)


# -------------------------------------------------
# 10. Print list elements using index
# -------------------------------------------------

fruits = ["apple", "banana", "mango"]
for i in range(len(fruits)):
    print(i, fruits[i])


# -------------------------------------------------
# 11. Numbers divisible by both 3 and 5 (1–100)
# -------------------------------------------------

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# -------------------------------------------------
# 12. Factorial of a number
# -------------------------------------------------

n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


# -------------------------------------------------
# 13. Fibonacci series (10 terms)
# -------------------------------------------------

n = 10
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b


# -------------------------------------------------
# 14. Find maximum in list
# -------------------------------------------------

numbers = [4, 7, 1, 9, 3]
max_val = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > max_val:
        max_val = numbers[i]
print("Max:", max_val)


# -------------------------------------------------
# 15. Print triangle pattern
# -------------------------------------------------

for i in range(1, 6):
    print("*" * i)


# -------------------------------------------------
# 16. Print prime numbers between 1 and 50
# -------------------------------------------------

for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# -------------------------------------------------
# 17. Reverse a number
# -------------------------------------------------

num = 1234
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed:", reverse)


# -------------------------------------------------
# 18. Count digits in a number
# -------------------------------------------------

num = 98765
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits:", count)


# -------------------------------------------------
# 19. Print pyramid pattern
# -------------------------------------------------

n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


# -------------------------------------------------
# 20. Multiples of 7 under 100 using list comprehension
# -------------------------------------------------

multiples = [i for i in range(1, 100) if i % 7 == 0]
print(multiples)


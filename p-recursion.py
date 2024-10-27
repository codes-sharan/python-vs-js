# recursion examples

# 1. Factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 2. Fibonacci Sequence

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

#3. Sum of a list
def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

print(recursive_sum([1, 2, 3, 4, 5]))  # Output: 15

# 4. Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Output: "olleh"

# 5. Power Calculation
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

print(power(2, 3))  # Output: 8


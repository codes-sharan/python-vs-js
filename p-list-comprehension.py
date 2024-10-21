# list comprehension (concise and powerful way to create lists in Python)
# syntactic shortcut for generating lists based on existing lists or other iterables.
# [expression for item in iterable if condition]
# expression: The value to include in the new list.
# item: The variable that takes the value of each element in the iterable.
# iterable: Any iterable (like a list, tuple, or range).
# condition (optional): A filter that determines whether to include the item.

# 1. simple list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

#2. using a condition
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4, 6]


# 3. Nested list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 4. Using functions
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)  # Output: [5, 5, 6]


# 5. Dictionary comprehension
numbers = [1, 2, 3]
squared_dict = {x: x ** 2 for x in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9}

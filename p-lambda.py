# Lambda function examples

# 1. Simple addition
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

# 2. Squaring a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# 3. Filtering with filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# 4. mapping with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# 5. Sorting with sorted
points = [(2, 3), (1, 2), (4, 1)]
sorted_points = sorted(points, key=lambda point: point[1])  # Sort by the second element
print(sorted_points)  # Output: [(4, 1), (1, 2), (2, 3)]

# 6. Using with reduce
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

# 7. Conditional expressions
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))  # Output: 20

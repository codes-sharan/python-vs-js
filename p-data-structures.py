# 1. Lists (ordered, mutable)
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[1])  # Output: banana

# Adding elements
fruits.append("orange")

# Removing elements
fruits.remove("banana")

print(fruits)  # Output: ['apple', 'cherry', 'orange']



# Tuples (ordered, immutable)
# Creating a tuple
coordinates = (10.0, 20.0)

# Accessing elements
print(coordinates[0])  # Output: 10.0

# Tuples cannot be modified
# coordinates[0] = 15.0  # This would raise an error



# 3.Sets (unordered collection of unique elements)
# Creating a set
colors = {"red", "green", "blue"}

# Adding elements
colors.add("yellow")

# Removing elements
colors.remove("green")

print(colors)  # Output: {'red', 'blue', 'yellow'}



# 4. Dictionaries (mutable, unordered collection of key-value pairs)
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: Alice

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Removing a key-value pair
del person["age"]

print(person)  # Output: {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}


# 5. Strings (immutable sequence of characters)
# Although strings are not a traditional data structure, they are important for text manipulation and can be treated as sequences.

# Creating a string
greeting = "Hello, World!"

# Accessing characters
print(greeting[0])  # Output: H

# Slicing
print(greeting[7:12])  # Output: World

# Strings are immutable
# greeting[0] = "h"  # This would raise an error

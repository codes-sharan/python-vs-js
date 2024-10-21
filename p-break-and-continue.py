# break and continue statement

# break

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

# Output: 0, 1, 2, 3, 4


# continue

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Output: 1, 3, 5, 7, 9

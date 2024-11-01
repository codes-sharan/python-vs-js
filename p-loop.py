# for loop
for i in range(5):
    print("Iteration:", i)


# while loop (cannot use count++ like in js)
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# simulating do while loop 
count = 1
while True:  # Create an infinite loop
    print(count)
    count += 1
    if count > 5:  # Condition checked at the end
        break

// break and continue statement

// break

for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break; // Exit the loop when i is 5
  }
  console.log(i);
}

// Output: 0, 1, 2, 3, 4

// continue
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    continue; // Skip even numbers
  }
  console.log(i);
}

// Output: 1, 3, 5, 7, 9

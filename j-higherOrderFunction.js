// A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result. Higher-order functions are a key concept in functional programming and are often used for tasks like function composition, transformation, and creating more abstract code.

//1.  higher-order function that takes a function as an argument

// Higher-order function
function applyOperation(operation, a, b) {
  return operation(a, b);
}

// A simple addition function
function add(x, y) {
  return x + y;
}

// A simple multiplication function
function multiply(x, y) {
  return x * y;
}

// Using the higher-order function
const sum = applyOperation(add, 5, 3); // Output: 8
const product = applyOperation(multiply, 5, 3); // Output: 15

console.log(`Sum: ${sum}`); // Output: Sum: 8
console.log(`Product: ${product}`); // Output: Product: 15

// 2. higher-order function that returns another function.

// Higher-order function that returns a function
function createMultiplier(factor) {
  return function (x) {
    return x * factor;
  };
}

// Create specific multiplier functions
const double = createMultiplier(2); // Multiplier for 2
const triple = createMultiplier(3); // Multiplier for 3

// Use the returned functions
console.log(double(5)); // Output: 10
console.log(triple(5)); // Output: 15

console.log(createMultiplier);

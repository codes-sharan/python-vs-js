// Arrow functions are a more concise way to write function expressions in JavaScript. Introduced in ECMAScript 6 (ES6), they provide a simpler syntax for defining functions.

// Syntax

// Regular function
function add(a, b) {
  return a + b;
}

// Arrow function
const sum = (a, b) => {
  return a + b;
};

// Differences
// 1. Syntax:

// Arrow functions can omit the function keyword and curly braces if they consist of a single expression, allowing for a more concise syntax:

const multiply = (a, b) => a * b; // Implicit return

// 2. Constructor Usage:

// Arrow functions cannot be used as constructors and will throw an error if you try to use new with them.
// Regular functions can be used as constructors.

// 3. arguments Object:

// Arrow functions do not have their own arguments object. You can still access arguments using rest parameters if needed.
// Regular functions have their own arguments object.

const arrowFunc = () => {
  console.log(arguments); // ReferenceError: arguments is not defined
};

function regularFunc() {
  console.log(arguments); // Works as expected
}

// 4. Implicit Return:

// Arrow functions allow for an implicit return of the value when using a single expression, which eliminates the need for the return keyword and curly braces.
// Regular functions require an explicit return statement.

// 5. this Context:

// Arrow functions do not have their own this context. They lexically bind this, meaning that this retains the value from the surrounding lexical context (the enclosing function or scope).
// Regular functions have their own this context, which depends on how they are called.

// Summary
// Arrow functions offer a more concise syntax, do not bind their own this, cannot be used as constructors, and do not have their own arguments object.
// They are particularly useful for callbacks, methods, and when you want to preserve the this context of the surrounding scope.

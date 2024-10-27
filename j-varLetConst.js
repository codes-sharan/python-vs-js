//
// The keywords let, const, and var are used for declaring variables in JavaScript, but they have different characteristics and behaviors. Here's a breakdown of the differences:

// 1. Scope

// Function-scoped or globally-scoped.
// If declared inside a function, it is accessible throughout that function. If declared outside any function, it becomes a global variable.

function example() {
  var x = 10; // x is function-scoped
}
console.log(x); // ReferenceError: x is not defined

// let and const:
// Block-scoped.
// They are only accessible within the block (enclosed by {}) in which they are defined.

if (true) {
  let y = 20; // y is block-scoped
  const z = 30; // z is also block-scoped
}
console.log(y); // ReferenceError: y is not defined
console.log(z); // ReferenceError: z is not defined

// 2. Reassignment
// var:
// Variables declared with var can be reassigned and redeclared within the same scope.
var a = 1;
var a = 2; // No error

// let:

// Variables declared with let can be reassigned but cannot be redeclared in the same scope.
let b = 1;
b = 2; // No error
// let b = 3; // SyntaxError: Identifier 'b' has already been declared

// const:

// Variables declared with const cannot be reassigned or redeclared. They must be initialized at the time of declaration.

const c = 1;
// c = 2; // TypeError: Assignment to constant variable
// const c = 3; // SyntaxError: Identifier 'c' has already been declared

// 3. Hoisting
// var:

// Variables declared with var are hoisted to the top of their function or global scope. They are initialized to undefined.

console.log(d); // Outputs: undefined
var d = 4;

// let and const:

// Variables declared with let and const are also hoisted but are not initialized. Accessing them before their declaration results in a ReferenceError due to the "temporal dead zone."

// console.log(e); // ReferenceError: Cannot access 'e' before initialization
let e = 5;

// Summary
// var: Function-scoped, can be redeclared and reassigned, hoisted with initialization to undefined.
// let: Block-scoped, can be reassigned but not redeclared in the same scope, hoisted but not initialized.
// const: Block-scoped, cannot be reassigned or redeclared, must be initialized at declaration, hoisted but not initialized.
// In general, it's recommended to use let and const for variable declarations in modern JavaScript due to their clearer scoping rules and prevention of accidental redeclaration. Use const by default, and only use let if you need to reassign the variable later.

// In JavaScript, there are six primitive data types:

// 1. String: Represents a sequence of characters. Strings can be created using single quotes, double quotes, or backticks (template literals).
let name = "John";
let greeting = "Hello, world!";
let template = `My name is ${name}.`;
console.log(template);
console.log(typeof template);

// 2. Number: Represents both integer and floating-point numbers. JavaScript does not differentiate between different types of numbers (like integers and floats).
let age = 30;
let price = 19.99;

console.log(typeof price);
console.log(typeof age);

// 3. Boolean: Represents a logical entity and can have two values: true or false
let isStudent = true;
let hasGraduated = false;
console.log(typeof isStudent);

// 4. Undefined: A variable that has been declared but has not yet been assigned a value is of type undefined.
let x;
console.log(x); // Outputs: undefined

// 5. Null: Represents the intentional absence of any object value. It is an assignment value.

let emptyValue = null;
console.log(typeof emptyValue); //it returns object !!(need to remember)

// 6. Symbol:  Introduced in ES6, symbols are unique and immutable identifiers. They are often used as object property keys to avoid name clashes.
const uniqueId = Symbol("id");
console.log(typeof uniqueId);
console.log(uniqueId); //returns Symbol(id)

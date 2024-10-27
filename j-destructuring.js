//1. Destructuring Arrays

const colors = ["red", "green", "blue"];

// Destructuring the array
const [firstColor, secondColor] = colors;

console.log(firstColor); // Output: 'red'
console.log(secondColor); // Output: 'green'

// Destructuring Objects

const person = {
  name: "Alice",
  age: 30,
  city: "New York",
};

//2. Destructuring the object
const { name, age } = person;

console.log(name); // Output: 'Alice'
console.log(age); // Output: 30

//3.  Default values
// You can also assign default values in case the property or index is undefined:
const numbers = [1, 2];

// Destructuring with a default value
const [firstNumber, secondNumber, thirdNumber = 3] = numbers;

console.log(firstNumber); // Output: 1
console.log(secondNumber); // Output: 2
console.log(thirdNumber); // Output: 3 (default value)

// 4. Nested Destructuring
const user = {
  id: 1,
  details: {
    name2: "Bob",
    age2: 25,
  },
};

// Nested destructuring
const {
  details: { name2, age2 },
} = user;

console.log(name2); // Output: 'Bob'
console.log(age2); // Output: 25

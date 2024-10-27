//1. Write a simple if statement to check if a number is even or odd.
let num = 5;
if (num % 2 == 0) {
  console.log(`${num} is even`);
} else {
  console.log(`${num} is odd`);
}

//2. How do you create a switch statement? Give an example.
let fruit = "apple";
let message;

switch (fruit) {
  case "apple":
    message = "You selected an apple!";
    break;
  case "banana":
    message = "You selected a banana!";
    break;
  case "orange":
    message = "You selected an orange!";
    break;
  case "grape":
    message = "You selected grapes!";
    break;
  default:
    message = "Fruit not recognized.";
}

console.log(message); // Output: You selected an apple!

//3. How do you declare a function in JavaScript? Write a function that takes two numbers and returns their sum.

function add(a = 0, b = 0) {
  return a + b;
}

const result = add(1, 2);

// Display results
console.log(`The sum result is: ${result}`);

// 4. How do you create an array in JavaScript? Write code to add an element to an array.

// i. Using Square brackets
const fruits = ["apple", "banana", "orange"];

// ii. Using Array constructor:
const fruits1 = new Array("apple", "mango", "pineapple");

// Adding an element to an array
fruits.push("grape"); //add to the end
fruits.unshift("litchi");
console.log(fruits);

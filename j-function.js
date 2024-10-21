// function (template literal is used)

function greet(name) {
  return `Hello, ${name}!`;
}

let message = greet("Hari");
console.log(message);

// arrow function

const greetA = () => {
  return "Hello, World!";
};

console.log(greetA());

// Arrow function single line

const greetASL = (name) => `Hello, ${name}!`;

let message1 = greet("Alice");
console.log(message1);

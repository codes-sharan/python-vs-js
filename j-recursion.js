const categories = [
  {
    name: "Motors, Tools & DIY",
    children: [
      {
        name: "Lubricants",
        children: null,
      },
      {
        name: "Motorcycles",
        children: [
          {
            name: "Standard Bikes",
            children: null,
          },
          {
            name: "Electric Bikes",
            children: null,
          },
          {
            name: "Scooters",
            children: null,
          },
        ],
      },
    ],
  },
];

// function printItems(cat) {
//   console.log(cat[0].name);
//   console.log(" ", cat[0].children[0].name);
//   console.log(" ", cat[0].children[1].name);
//   console.log("     ", cat[0].children[1].children[0].name);
//   console.log("     ", cat[0].children[1].children[1].name);
//   console.log("     ", cat[0].children[1].children[2].name);
// }

// printItems(categories);

const printName = (name) => {
  console.log(name);
};

const spaceCalc = (i) => {
  let gap = "";
  for (let j = 0; j < i; j++) {
    gap += "    ";
  }
  return gap;
};
// [{children: [{},{},{}]}, {}, {}]
const printCategories = (catList, i = 0) => {
  let gap = spaceCalc(i);
  for (let cat of catList) {
    printName(gap + cat.name);
    if (cat.children) {
      i++;
      printCategories(cat.children, i);
    }
  }
};

printCategories(categories);

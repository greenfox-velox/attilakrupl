const planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true,
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true,
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true,
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false,
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true,
  },
];

// Remove the king from the list.
const theList = document.querySelector('ul');
theList.removeChild(document.querySelector('li'));
// Fill the list based on the following list of objects:
for (let i = 0; i < planetData.length; i++) {
  if (planetData[i].asteroid === true) {
    const newElement = document.createElement('li');
    newElement.classList.add(planetData[i].category);
    newElement.textContent = planetData[i].content;
    theList.appendChild(newElement);
  }
}
// only add the asteroids to the list.
// each list item should have its category as a class
// and its content as text content.

// Remove the king from the list.
const listElements = document.querySelector('ul');
listElements.removeChild(document.querySelector('li'));
// Add 3 list items saying 'The Fox' to the list.

for (let i = 0; i < 3; i++) {
  const newElement = document.createElement('li');
  newElement.textContent = 'The Fox';
  listElements.appendChild(newElement);
}

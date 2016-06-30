// Remove the king from the list.
const theList = document.querySelector('ul');
theList.removeChild(document.querySelector('li'));
// Add list items that have the following text contents:
// ['apple', 'bubble', 'cat', 'green fox']
const contentList = ['apple', 'bubble', 'cat', 'green fox'];

for (let i = 0; i < contentList.length; i++) {
  const newElement = document.createElement('li');
  newElement.textContent = contentList[i];
  theList.appendChild(newElement);
}

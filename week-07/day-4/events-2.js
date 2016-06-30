// On the click of the button,
// Count the items in the list
// And display the result in the result element.
const theButton = document.querySelector('button');
function actionNow() {
  const listItems = document.querySelectorAll('li');
  document.querySelector('.result').innerHTML = listItems.length;
}
theButton.addEventListener('click', actionNow);

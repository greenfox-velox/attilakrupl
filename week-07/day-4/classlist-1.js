// Does the third p have a cat class?
// If so, alert 'YEAH CAT!'
const ps = document.querySelectorAll('p');
if (ps[2].classList.value === 'cat') {
  alert('YEAH CAT!');
}
// If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
if (ps[3].classList.value === 'dolphin') {
  document.querySelectorAll('p')[0].innerHTML = 'pear';
}
// If the first p has an 'apple' class, replace cat's content with 'dog'
if (ps[0].classList.value === 'apple') {
  document.querySelectorAll('p')[0].innerHTML = 'pear';
}
// Make apple red
document.querySelector('.apple').classList.add('red');
// Make balloon less balloon-like
document.querySelector('.balloon').classList.remove('balloon');

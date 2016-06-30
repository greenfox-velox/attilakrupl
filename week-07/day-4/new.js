'use strict';
// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.
const king = document.querySelector('#b325');
console.log(king);
// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.
const conceited = document.querySelector('.asteroid.b326');
alert(conceited);
// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.
const businessLamp = document.querySelectorAll('.big');
for (let i = 0; i < businessLamp.length; i++) {
  let x = 0;
  // console.log(businessLamp[x]);
  x++;
}
// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.
const conceitedKing = document.querySelectorAll('.container .asteroid');
for (let j = 0; j < conceitedKing.length; j++) {
  alert(conceitedKing[j]);
}
// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.
const noBusiness = document.querySelectorAll('div.asteroid');
for (let i = 0; i < noBusiness.length; i++) {
  console.log(noBusiness[i]);
}
// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.
const allBizniss = document.querySelectorAll('p.asteroid');
for (let i = 0; i < allBizniss.length; i++) {
  alert(allBizniss[i]);
}

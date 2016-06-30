'use strict';

const fileList = ['./images/01.jpg',
                  './images/02.jpg',
                  './images/03.jpg',
                  './images/04.jpg',
                  './images/05.jpg',
                  './images/06.jpg',
                  './images/07.jpg',
                  './images/08.jpg',
                  './images/09.jpg',
                  './images/10.jpg'];

const startingSetting = new function() {
  document.querySelector('.main-image').setAttribute('src', fileList[0]);
};

console.log(document.querySelectorAll('.thumbnail'));
document.querySelectorAll('.thumbnail')[0].setAttribute('src', fileList[0]);
document.querySelectorAll('.thumbnail')[1].setAttribute('src', fileList[1]);
document.querySelectorAll('.thumbnail')[2].setAttribute('src', fileList[2]);
document.querySelectorAll('.thumbnail')[3].setAttribute('src', fileList[3]);
document.querySelectorAll('.thumbnail')[4].setAttribute('src', fileList[4]);

'use strict';
// const fs = require('fs');
// function getFiles(dir) {
//   const fileList = [];
//   const files = fs.readdirSync(dir);
//   for (var i in files) {
//     if (!files.hasOwnProperty(i)) continue;
//     const name = dir+'/'+files[i];
//     if (!fs.statSync(name).isDirectory()) {
//       fileList.push(name);
//     }
//   }
//   return fileList;
// }
// const fileList = getFiles('/images');
// console.log(fileList);
let imageCounter = 0;
let thumbCounter = 0;
const fileList = ['Ceres-Bright-Spot',
                  'Saturn',
                  'Saturn-F-Ring',
                  'Epimetheus',
                  'Enceladus',
                  'Ceres-Ridges',
                  'Enceladus-Tectonic',
                  'Saturn-Rings',
                  'Saturn-Rings-2',
                  'Dione'];
const numOfImages = fileList.length;
const bigButtonLeft = document.querySelector('#button1');
const bigButtonRight = document.querySelector('#button2');
const smallButtonLeft = document.querySelector('#button3');
const smallButtonRight = document.querySelector('#button4');
// const thumb1 = document.querySelector('#thumb1');
// const thumb2 = document.querySelector('#thumb2');
// const thumb3 = document.querySelector('#thumb3');
// const thumb4 = document.querySelector('#thumb4');
// const thumb5 = document.querySelector('#thumb5');

function fileNameGenerator(num) {
  const fileName = fileList[((imageCounter) + num) % numOfImages];
  return './images/' + fileName + '.jpg';
}

function thumbNameGenerator(num) {
  const fileName = fileList[((thumbCounter) + num) % numOfImages];
  return './images/' + fileName + '.jpg';
}

function setName() {
  document.querySelector('.image_name').textContent = fileList[imageCounter % numOfImages];
}

function setImages() {
  document.querySelectorAll('.main-image')[0].setAttribute('src', fileNameGenerator(0));
  for (let i = 0; i < 5; i++) {
    document.querySelectorAll('.thumbnail')[i].setAttribute('src', fileNameGenerator(i));
  }
  document.querySelectorAll('.thumbnail')[0].classList.add('highlighted');
}

function moveImages() {
  document.querySelectorAll('.main-image')[0].setAttribute('src', fileNameGenerator(0));
  thumbCounter = imageCounter;
}

function moveThumbs() {
  for (let i = 0; i < 5; i++) {
    document.querySelectorAll('.thumbnail')[i].setAttribute('src', thumbNameGenerator(i));
  }
}


function goLeft() {
  if (imageCounter > 0) {
    imageCounter--;
  } else {
    imageCounter += numOfImages - 1;
  }
  moveImages();
  moveThumbs();
  setName();
}

function goRight() {
  imageCounter++;
  moveImages();
  moveThumbs();
  setName();
}

function thumbLeft() {
  if (thumbCounter > 0) {
    thumbCounter--;
  } else {
    thumbCounter += numOfImages - 1;
  }
  moveThumbs();
}

function thumbRight() {
  thumbCounter++;
  moveThumbs();
}

// function highlightThumb(id) {
//   for (let i in document.querySelectorAll('.thumbnail')) {
//     i.classList.remove('highlighted');
//   }
//   document.querySelector(id).classList.add('highlighted');
// }

setImages();
setName();
bigButtonLeft.addEventListener('click', goLeft);
bigButtonRight.addEventListener('click', goRight);
smallButtonLeft.addEventListener('click', thumbLeft);
smallButtonRight.addEventListener('click', thumbRight);
// thumb1.addEventListener('click', goLeft);

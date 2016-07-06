'use strict';

const fs = require('fs');

// function longerThanZero(word) {
//   return word.length > 0;
// }
//
// function count(cont1) {
//   const re = /\s+/g/;
//   const lstOfWords = String(cont1).split(re);
//   const filtered = lstOfWords.filter(longerThanZero);
//   return filtered.length;
// }
//
// function readThis(fileName) {
//   fs.readFile(fileName, function(err, cont1){
//     console.log(count(cont1));
//   });
// }
//
// readThis('alma.txt');

function wordCount(fileName, cb) {
  fs.readFile(fileName, function(err, content) {
    if (err) {
      return cb(err);
    }
    const count = String(content).split(/\s/g).length;
    cb(err, count);
  });
}


wordCount('alma.txt', function(err,c) {
  console.log(err, c);
})


// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

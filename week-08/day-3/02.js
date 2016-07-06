'use strict';
var fs = require('fs');
// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
//

function countLetters(fileName, letter, cb) {
  fs.readFile(fileName, function(err, content) {
    if (err) {
      return err;
    }
    let count = 0;
    String(content).split('').forEach(function(e) {
      if (e === letter) {
        count++;
      }
    });
    cb(err, count);
  });
}

countLetters('alma.txt', 'a', function(err, result) {
  console.log(err, result)
});

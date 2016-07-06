'use strict';
var fs = require('fs');

function fileConcatenator(file1, file2, cb) {
  fs.readFile(file1, function(error, content1) {
    if (error) {
      return cb(error);
    }
    fs.readFile(file2, function(error, content2){
      if (error) {
        return cb(error);
      }
      cb(String(content1) + String(content2));
    });
  });
}

fileConcatenator('alma.txt', 'korte.txt', function(error, contents) {
  if (error) {
    console.log(error);
  } else {
    console.log(contents);
  }
});

// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error

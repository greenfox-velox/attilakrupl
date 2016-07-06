'use strict';
var fs = require('fs');
const fileNames = ['alma.txt', 'korte.txt'];
// create a function that has 2 paramteres
//  - fileNames: an array of filenames
//  - callback
//
// it should read the files and call the callback with their content concated
// it should have the same order as the filenames
// it should pass the error as a parameter


fileConcatenator(fileNames, function(error, content){
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
})

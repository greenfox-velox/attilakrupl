'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

var myFunction = function(num) {
  switch(num){
    case 0:
    console.log('zero');
    break;
    case 1:
    console.log('one');
    break;
    case 2:
    console.log('two');
    break;
    case 3:
    console.log('three');
    break;
    case 4:
    console.log('four');
    break;
    default:
    console.log('many');
    break;
  }
}

myFunction(2)
myFunction(6)

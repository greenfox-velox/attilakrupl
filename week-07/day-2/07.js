'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise


var checkArray = function(arr){
  return arr.every(function(e){
    if (e < 2) return false;
    var q = Math.floor(Math.sqrt(e));
    for (var i = 2; i <= q; i++) {
        if (e % i == 0) {
            return false;
        }
    }
    return true;
  });
}

console.log(checkArray(numbers));

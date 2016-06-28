'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 2, p: 2, l: 1}

var myFunc = function(str){
  var myObj = new Object();
  str.split('').forEach(function(e){
    if (e in myObj){
      myObj[e]++
    } else {
      myObj[e] = 1
    }
  })
  return myObj;
}

console.log(myFunc("apple"))

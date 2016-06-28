'use strict';

// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

var myfunc = function(str, char){
  var val = false;
  var strSpl = str.split("");
  strSpl.forEach(function(e){
    if (e === char){
      val = true;
    }
  })
  return val;
}

console.log(myfunc("alma", 'l'));

'use strict';

var apply = function(fun){
  fun("apple")
}

// create a function called apply that takes a function and calls it with one argument
// that is the string 'apple'

apply(console.log) // should log apple

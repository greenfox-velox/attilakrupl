'use strict';

function addNumbers() {
  return [1, 2, 3, 4, 5, 6].reduce(function name (result, number){
    return result + number;
  }, 0);
}

console.log(addNumbers());

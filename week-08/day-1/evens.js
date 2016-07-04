'use strict';

const numbers = [1, 2, 3, 4, 5, 6, 7];

const evens = numbers.reduce(function(acc, e) {
  if (e % 2 === 0) {
    acc.push(e);
  }
  return acc;
}, []);

console.log(evens);

'use strict';

function listChars(str) {
  return str.split('').reduce(function(acc, e) {
  acc[e] = acc[e] + 1 || 1;
    return acc;
  }, {});
}
// console.log(listChars('apple'));

module.exports.listChars = listChars;

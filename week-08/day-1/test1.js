'use strict';
const listChars = require('./01');
const tape = require('tape');

tape(function(t) {
  t.deepEqual(listChars.listChars('apple'), { a: 1, p: 2, l: 1, e: 1 });
  t.end();
});
console.log(listChars);

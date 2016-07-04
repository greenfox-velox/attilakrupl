'use strict';
const countBooks = require('./02');
const tape = require('tape');

tape(function(t) {
  t.deepEqual(countBooks.countBooks(countBooks.students), 4);
  t.end();
});

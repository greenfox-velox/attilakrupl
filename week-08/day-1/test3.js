'use strict';
const Rectangles = require('./03');
const tape = require('tape');

tape(function(t) {
  const rect = new Rectangles.Rectangles(2, 5);
  t.deepEqual(rect.getArea(), 10);
  t.deepEqual(rect.getCircumference(), 14);
  t.end();
});

'use strict';

// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(a, b) {
  this.a = a;
  this.b = b;
}
Rectangles.prototype.getArea = function() {
  return this.a * this.b;
};

Rectangles.prototype.getCircumference = function() {
  return 2 * (this.a + this.b);
};
const rect = new Rectangles(22, 15);
console.log(rect.getArea());
console.log(rect.getCircumference());

module.exports.Rectangles = Rectangles;
module.exports.getArea = Rectangles.prototype.getArea;
module.exports.getArea = Rectangles.prototype.getCircumference;

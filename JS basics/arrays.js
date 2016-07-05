const fruits = ['Apple', 'Banana'];
const newLength = fruits.push("Orange");
var last = fruits.pop();
console.log(last);

var first = fruits.shift(); // remove Apple from the front
console.log(fruits);

var newLength = fruits.unshift("Strawberry") // add to the front

fruits.push("Mango");

var pos = fruits.indexOf("Banana");

var removedItem = fruits.splice(pos, 1); // this is how to remove an item

var shallowCopy = fruits.slice(); // this is how to make a copy

console.log(Object.keys(fruits)); //this is how to get indexes

var num1 = [1, 2, 3],
    num2 = [4, 5, 6],
    num3 = [7, 8, 9];
var nums = num1.concat(num2, num3);
console.log(nums); // Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

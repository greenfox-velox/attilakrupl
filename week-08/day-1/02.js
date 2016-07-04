'use strict';


var students = [
  { name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings'] },
  { name: 'Ryan', age: 11, books: ['The funcdation'] },
  { name: 'Sheela', age: 14 },
  { name: 'Charlee', age: 9, books: [] },
  { name: 'Jessica', age: 12, books: ['Dune'] },
  { name: 'Robert', age: 15 }
];

function countBooks(array) {
  return array.reduce(function(counter, stud){
    return counter + ((stud.books && stud.books.length) || 0);
  }, 0);
}
// create a function that counts all the books of an array of students
// not every student has a property called books

module.exports.countBooks = countBooks;
module.exports.students = students;

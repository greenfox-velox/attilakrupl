'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack(){
  this.st = [],
  this.sze = 0,
  this.size = function(){
    return this.sze;
  },
  this.push = function(element){
    this.st[this.sze] = element;
    this.sze++
  },
  this.pop = function(){
    var that = this.st[this.sze-1];
    this.st = this.st.slice(0,this.sze-2);
    this.sze--
    return that;
  }
}

var myStack = new Stack();

myStack.push("blabvla");
console.log(myStack.size());
console.log(myStack.st);
console.log(myStack.pop());
console.log(myStack.size());
console.log(myStack.st);

'use strict';

var tape = require('tape');
var carPark = require('./04');
var Car = carPark.Car;

tape('Car properties', (t) => {
  const car = new Car('volvo', 'red', 50);
  t.equal(car.type, 'volvo');
  t.equal(car.color, 'red');
  t.equal(car.balance, 50);
  t.end();
});

tape('enter method', (t) => {
  const car = new Car('volvo', 'red', 50);
  car.enter(0);
  t.equal(car.enterDate, 0);
  t.end();
});

tape('getEnterDate method', (t) => {
  const car = new Car('volvo', 'red', 50);
  car.enter(1000);
  t.equal(car.enterDate, 1000);
  t.end();
});

tape('leave method', (t) => {
  const car = new Car('volvo', 'red', 50);
  car.leave(20);
  t.equal(car.balance, 30);
  t.end();
});

tape('getStats method', (t) => {
  const car = new Car('volvo', 'red', 50);
  t.equal(car.getStats(), 'Type: volvo, Color: red, Balance: 50');
  t.end();
});

tape('Car id ', (t) => {
  const car = new Car('volvo', 'red', 50);
  t.equal(typeof car.id, 'number');
  t.end();
});

tape('Car distinct ids ', (t) => {
  const car = new Car('volvo', 'red', 50);
  const car2 = new Car('ifa', 'blue', 10);
  t.notEqual(car.id, car2.id);
  t.end();
});

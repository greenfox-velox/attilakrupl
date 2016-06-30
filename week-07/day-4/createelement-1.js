'use strict';
// Add an item that says 'The Green Fox' to the asteroid list.
const asteroidList = document.querySelector('ul.asteroids');
const newAsteroid = document.createElement('li');
newAsteroid.innerHTML = 'The Green Fox';
asteroidList.appendChild(newAsteroid);
// Add an item that says 'The Lamplighter' to the asteroid list.
const lamplighter = document.createElement('li');
lamplighter.innerHTML = 'The Lamplighter';
asteroidList.appendChild(lamplighter);
// Add a heading saying 'I can add elements to the DOM!' to the .container.
const theContainer = document.querySelector('div.container');
const newHeading = document.createElement('h1');
newHeading.innerHTML = 'I can add elements to the DOM!';
theContainer.appendChild(newHeading);
// Add an image, any image, to the container.
const newImage = document.createElement('img');
newImage.setAttribute('src', 'https://i.ytimg.com/vi/OmCxtWrRQJ8/maxresdefault.jpg');
theContainer.appendChild(newImage);

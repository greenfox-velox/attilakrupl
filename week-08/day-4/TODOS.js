'use strict';

var addButton = document.querySelector('.add_task');
var childList = [];


function createTaskElements(e) {
  var task = document.createElement('div');
  var todoItem = document.createElement('div');
  var dothis = document.createElement('p');
  var imgCont = document.createElement('div');
  var bin = document.createElement('button');
  var chckbx = document.createElement('button');

  task.setAttribute('id', e.id);
  dothis.innerHTML = e.text;
  imgCont.className = 'img_cont';
  bin.className = 'bin';
  bin.setAttribute('id', e.id);
  bin.addEventListener('click', removeTask);
  chckbx.className = 'checkbox ' + e.id;
  chckbx.setAttribute('id', e.completed ? 'checked' : 'unchecked');

  imgCont.appendChild(bin);
  imgCont.appendChild(chckbx);
  todoItem.appendChild(dothis);
  task.appendChild(todoItem);
  task.appendChild(imgCont);
  document.querySelector('.tasks').appendChild(task);
  childList.push(task);
}

function dispCont() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var all = JSON.parse(xhr.responseText);
    var myNode = document.querySelector('.tasks');
    myNode.innerHTML = '';
    all.forEach((e) => {
      createTaskElements(e);
    });
  };
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.send();
}

function removeTask() {
  console.log(event.target.id);
  var xhr = new XMLHttpRequest();
  var deleteID = event.target.id;
  var reqURL = 'https://mysterious-dusk-8248.herokuapp.com/todos/' + deleteID;
  xhr.open('DELETE', reqURL);
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      dispCont();
    }
  };
  xhr.send();
}

function addTask() {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  var content = document.querySelector('#content');
  var sendThis = content.value;
  var newTask = JSON.stringify({ text: sendThis });
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      dispCont();
    }
  };
  xhr.send(newTask);
}

dispCont();
addButton.addEventListener('click', addTask);

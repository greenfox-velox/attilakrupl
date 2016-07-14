'use strict';

var addButton = document.querySelector('.add_task');
var childList = [];
var url = 'http://localhost:3000/todos/';

function createTaskElements(e) {
  var task = document.createElement('div');
  var todoItem = document.createElement('div');
  var dothis = document.createElement('p');
  var imgCont = document.createElement('div');
  var edit = document.createElement('button');
  var bin = document.createElement('button');
  var chckbx = document.createElement('button');

  task.setAttribute('id', e.id);
  dothis.innerHTML = e.text;
  dothis.setAttribute('id', 't' + e.id)
  dothis.className = e.completed ? 'check' : '';
  imgCont.className = 'img_cont';
  edit.className = 'edit';
  edit.setAttribute('id', e.id);
  edit.addEventListener('click', editTask);
  bin.className = 'bin';
  bin.setAttribute('id', e.id);
  bin.addEventListener('click', removeTask);
  chckbx.className = 'checkbox ' + (e.completed ? 'checked' : 'unchecked');
  chckbx.addEventListener('click', checkUncheck);
  chckbx.setAttribute('id', e.id);

  imgCont.appendChild(edit);
  imgCont.appendChild(bin);
  imgCont.appendChild(chckbx);
  todoItem.appendChild(dothis);
  task.appendChild(todoItem);
  task.appendChild(imgCont);
  document.querySelector('.tasks').appendChild(task);

  childList.push(task);
}

function clearScreenContent() {
  var myNode = document.querySelector('.tasks');
  myNode.innerHTML = '';
}

function displayContent() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var all = JSON.parse(xhr.responseText);
    clearScreenContent();
    all.forEach((e) => {
      createTaskElements(e);
    });
  };
  xhr.open('GET', url);
  xhr.send();
}

function removeTask() {
  var xhr = new XMLHttpRequest();
  var deleteID = event.target.id;
  var reqURL = url + deleteID;
  xhr.open('DELETE', reqURL);
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      displayContent();
    }
  };
  xhr.send();
}

function checkUncheck() {
  var xhr = new XMLHttpRequest();
  var id = event.target.id;
  var readyOrNot = event.target.classList[1];
  var setToThis = readyOrNot === 'checked' ? 0 : 1;
  var text = document.querySelector('#t' + event.target.id).innerHTML;
  var request = {
    'text': text,
    'completed': setToThis,
  };
  var JSONReq = JSON.stringify(request);
  var reqURL = url + id;
  xhr.open('PUT', reqURL);
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      displayContent();
    }
  };
  xhr.send(JSONReq);
}

function clear() {
  var content = document.querySelector('#content');
  document.querySelector('#content').value = '';
}

function addTask() {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', url);
  var content = document.querySelector('#content');
  var sendThis = content.value;
  var newTask = JSON.stringify({ text: sendThis });
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      displayContent();
    }
  };
  clear();
  xhr.send(newTask);
}

function editTask() {
  var xhr = new XMLHttpRequest();
  var id = event.target.id;
  var readyOrNot = event.target.classList[1];
  var setToThis = readyOrNot === 'checked' ? true : false;
  var text = document.querySelector('#t' + event.target.id).innerHTML;
  var changeTaskToThis = prompt('Enter the updated task!', text);
  var request = {
    'text': changeTaskToThis,
    'completed': setToThis,
  };
  var JSONReq = JSON.stringify(request);
  var reqURL = url + id;
  xhr.open('PUT', reqURL);
  xhr.setRequestHeader('content-type', 'application/json; charset=utf-8');
  xhr.send(JSONReq);
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      displayContent();
    }
  };
}
displayContent();
addButton.addEventListener('click', addTask);

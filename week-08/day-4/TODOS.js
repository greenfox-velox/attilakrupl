'use strict';

var addButton = document.querySelector('.add_task');

function dispCont() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var all = JSON.parse(xhr.responseText);
    all.forEach((e) => {
      var task = document.createElement('div');
      var todo_item = document.createElement('div');
      var dothis = document.createElement('p');
      var img_cont = document.createElement('div');
      var img1 = document.createElement('div');
      var bin = document.createElement('button');
      var img2 = document.createElement('div');
      var chckbx = document.createElement('button');

      task.className = 'task';
      task.setAttribute('id', e.id);
      todo_item.className = 'todo-item';
      dothis.innerHTML = e.text;
      img_cont.className = 'img_cont';
      bin.className = 'bin';
      bin.setAttribute('alt', 'bin');
      chckbx.className = 'checkbox';
      if (e.completed === false) {
        chckbx.setAttribute('id', 'unchecked');
        chckbx.setAttribute('alt', 'unchecked');
      } else {
        chckbx.setAttribute('id', 'checked');
        chckbx.setAttribute('alt', 'checked');
      }

      img2.appendChild(chckbx);
      img1.appendChild(bin);
      img_cont.appendChild(img1);
      img_cont.appendChild(img2);
      todo_item.appendChild(dothis);
      task.appendChild(todo_item);
      task.appendChild(img_cont);
      document.querySelector('.tasks').appendChild(task);
    });
  };
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.send();
}

dispCont();

addButton.addEventListener('click', dispCont);

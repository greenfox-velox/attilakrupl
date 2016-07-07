'use strict';

var submitButton = document.querySelector('.yodanize');
var content = document.querySelector('#content');
var h1 = document.querySelector('h1');
function doYodanize() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var data = xhr.responseText;
    h1.textContent = data;
  };
  var urlStr = 'https://yoda.p.mashape.com/yoda?sentence=' + encodeURIComponent(content.value);
  xhr.open('GET', urlStr);
  xhr.setRequestHeader('X-Mashape-Key', 'aWZATve9ITmshHjxNKyv2F4gHbltp1OCLxWjsnoB2JvmXPMzik');
  xhr.send();
}
submitButton.addEventListener('click', doYodanize);

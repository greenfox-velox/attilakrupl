'use strict';

const runTheRequest = document.querySelector('.run_the_request');
const arr1 = [];

function doRequest() {
  arr1.push(document.querySelector('.request_script').src = 'req.js');
  
}


runTheRequest.addEventListener('click', doRequest);

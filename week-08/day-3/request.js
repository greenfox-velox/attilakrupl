'use strict';

const runTheRequest = document.querySelector('.run_the_request');
const arr1 = [];

function doRequest() {
  (document.querySelector('.request_script').src = 'req.js');
}


runTheRequest.addEventListener('click', doRequest);

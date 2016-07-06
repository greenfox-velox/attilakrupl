
const xhr = new XMLHttpRequest();
xhr.onload = () => {
  console.log(xhr.response);
};
xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2015/6/27')
xhr.send();

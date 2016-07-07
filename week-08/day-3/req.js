
const xhr = new XMLHttpRequest();
xhr.onload = () => {
  let data = JSON.parse(xhr.response);
  console.log(data);
  alert(data.weekday);
  alert(data.celebrations.length);
};
xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2015/6/27')
xhr.send();

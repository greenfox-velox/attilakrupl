const theButton = document.querySelector('button');
function partyEvent() {
  if (document.querySelector('div').classList.contains('party')) {
    document.querySelector('div').classList.remove('party');
  } else {
    document.querySelector('div').classList.add('party');
  }
}
theButton.addEventListener('click', partyEvent);

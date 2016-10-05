'use strict';

var shift = 25;
var text = "Attila Krupl";

function decode(shift, text) {
  console.log(shift);
  var resolution = [];
  console.log(text.split(''));
  text.split('').forEach((char) => {
    if (char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90) {
      resolution.push(String.fromCharCode(((char.charCodeAt(0) - 65 + shift) % 25) + 65));
    } else if (char.charCodeAt(0) >= 97 && char.charCodeAt(0) <= 122) {
      resolution.push(String.fromCharCode(((char.charCodeAt(0) - 97 + shift) % 25) + 97));
    } else {
      resolution.push(char);
    }
  });

  console.log({ status: 'ok', text: resolution.join('') });
}

decode(shift, text);

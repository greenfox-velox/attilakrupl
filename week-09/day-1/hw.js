const http = require('http');
const server = http.createServer(function (req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  var r = new Date();
  res.end(req.url + ' ' +  r.getTime() % 86400000 + ' ' + req.method);
});

server.listen(3000, '127.0.0.1');
console.log('yo dawgs, now listening to port 3000');

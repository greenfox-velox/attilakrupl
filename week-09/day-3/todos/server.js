const mysql = require('mysql');
const express = require('express');
const bodyParser = require('body-parser');
const con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma123',
  database: 'todos',
});
const app = express();
app.use(bodyParser.json());
app.use(express.static('todo'));

// function errorHandling(res, item) {
//   if (item === undefined) {
//     res.sendStatus(404);
//   } else {
//     res.send(item);
//   }
// }

app.get('/todos', (req, res) => {
  con.query('SELECT * from todos WHERE destroyed = 0;', (err, rows) => {
  if (err) {
    console.log(err.toString());
    return;
  }
  res.send(JSON.parse(JSON.stringify(rows)));
  });
});

app.get('/todos/:id', (req, res) => {
  con.query('SELECT * from todos WHERE id = ?', req.params.id, (err, rows) => {
  if (err) {
    console.log(err.toString());
    return;
  }
  res.send(JSON.stringify(rows));
  });
});

app.post('/todos/', (req, res) => {
  var newLine = { completed : 0 , text:  req.body.text , destroyed : 0 };
  con.query('INSERT INTO todos SET ?', newLine, (err, rows) => {
  if (err) {
    console.log(err.toString());
    return;
  }
  res.send(JSON.stringify(rows));
  });
});

app.put('/todos/:id', (req, res) => {
  var newObj = (JSON.parse(JSON.stringify(req.body)));
  var setTo = newObj.completed ? 1 : 0;
  con.query('UPDATE todos SET text = ?, completed = ? Where ID = ?',
  [newObj.text, setTo, req.params.id], (err, rows) => {
  if (err) {
    console.log(err.toString());
    return;
  }
  res.send(JSON.stringify(rows));
  });
});

app.delete('/todos/:id', (req, res) => {
  con.query('UPDATE todos SET destroyed = ? Where ID = ?', [1, req.params.id], (err, result) => {
    if (err) {
      throw err;}
    res.send(JSON.stringify(result));
  });
});

app.listen(3000);

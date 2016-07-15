const mysql = require('mysql');
const express = require('express');
const bodyParser = require('body-parser');
const subFunctions = require('./subFunctions');

const con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma123',
  database: 'todos',
});

const app = express();

app.use(bodyParser.json());
app.use(express.static('todo'));

app.get('/todos', (req, res) => {
  con.query('SELECT * from todos WHERE destroyed = 0;', (err, rows) => {
  subFunctions.errorHandling(err);
  res.send(rows);
  });
});

app.get('/todos/:id', (req, res) => {
  con.query('SELECT * from todos WHERE id = ?', req.params.id, (err, rows) => {
  subFunctions.errorHandling(err);
  res.send(rows);
  });
});

app.post('/todos/', (req, res) => {
  con.query('INSERT INTO todos SET ?', subFunctions.setNewTodo(req.body.text), (err, rows) => {
  subFunctions.errorHandling(err);
  res.send(rows);
  });
});

app.put('/todos/:id', (req, res) => {
  con.query('UPDATE todos SET text = ?, completed = ? Where ID = ?',
  [subFunctions.defineBody(req.body).text, subFunctions.checkOrUncheck(req.body), req.params.id], (err, rows) => {
  subFunctions.errorHandling(err);
  res.send(rows);
  });
});

app.delete('/todos/:id', (req, res) => {
  con.query('UPDATE todos SET destroyed = ? Where ID = ?', [1, req.params.id], (err, result) => {
    subFunctions.errorHandling(err);
    res.send(result);
  });
});

app.listen(3000);

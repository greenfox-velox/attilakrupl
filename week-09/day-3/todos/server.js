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
const data = [
  {
    completed: false,
    id: 1,
    text: 'vasarolj tejet',
  },
  {
    completed: false,
    id: 2,
    text: 'fozz ebedet',
  },
  {
    completed: false,
    id: 3,
    text: 'mentsd meg a vilagot',
  },
];

let counter = data.length;

function errorHandling(res, item) {
  if (item === undefined) {
    res.sendStatus(404);
  } else {
    res.send(item);
  }
}

app.get('/todos', (req, res) => {
  con.query('SELECT * from todos;', (err, rows) => {
  if (err) {
    console.log(err.toString());
    return;
  }
  res.send(JSON.parse(JSON.stringify(rows)));
  });
});

app.get('/todos/:id', (req, res) => {
  var task = data.filter(e => {
    if (parseInt(e.id, 10) === parseInt(req.params.id, 10)) {
      return e;
    } })[0];
  console.log(task);
  res.send(task);
});

app.post('/todos/', (req, res) => {
  counter++;
  const bit = { completed: false, id: counter, text: req.body.text };
  data.push(bit);
  res.send(data);
});

app.put('/todos/:id', (req, res) => {
  var task = data.filter(e => {
    if (parseInt(e.id, 10) === parseInt(req.params.id, 10)) {
      return e;
    } })[0];
  if (task.completed) {
    task.completed = false;
  } else {
    task.completed = true;
  }
  task.text = req.body.text;
  res.send(task);
});

app.delete('/todos/:id', (req, res) => {
  const item = data.filter(e => {
    if (e.id === +req.params.id) {
      return e;
    }
  })[0];
  item.destroyed = true;
  data.splice(data.indexOf(item), 1);
  errorHandling(res, item);
});

app.listen(3000);

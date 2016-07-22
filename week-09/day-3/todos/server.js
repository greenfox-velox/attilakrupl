const express = require('express');
const bodyParser = require('body-parser');

const mysqlDB = require('./mysqlDB');

const app = express();

app.use(bodyParser.json());
app.use(express.static('todo'));

app.get('/todos', (req, res) => {
  mysqlDB.getTodos(req, row => {
    res.send(row);
  });
});

app.get('/todos/:id', (req, res) => {
  mysqlDB.getTodoByID(req, row => {
    res.send(row);
  });
});

app.post('/todos/', (req, res) => {
  mysqlDB.postTodo(req, row => {
    console.log(row);
    res.send(row);
  });
});

app.put('/todos/:id', (req, res) => {
  mysqlDB.modifyTodo(req, row => {
    res.send(row);
  });
});

app.delete('/todos/:id', (req, res) => {
  mysqlDB.deleteTodo(req, row => {
    res.send(row);
  });
});

app.listen(3000);

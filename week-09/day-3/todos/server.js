const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
app.use(express.static('todo'));
const data = [
  {
    completed: false,
    id: 1,
    text: 'Buy milk',
  },
  {
    completed: false,
    id: 2,
    text: 'Make dinner',
  },
  {
    completed: false,
    id: 3,
    text: 'Save the world',
  },
];

let counter = data.length;

app.get('/todos', (req, res) => {
  res.send(data);
});

app.get('/todos/:id', (req, res) => {
  res.send(data.filter(e => {
    if (parseInt(e.id, 10) === parseInt(req.params.id, 10)) {
      return e;
    } }));
});

app.post('/todos/', (req, res) => {
  counter++;
  const bit = { completed: false, id: counter, text: req.body.text };
  data.push(bit);
  res.send(data);
});

app.put('/todos/:id', (req, res) => {
  res.send(data.filter(e => {
    if (parseInt(e.id, 10) === parseInt(req.params.id, 10)) {
      e.completed = true;
      e.text = req.body.text;
    } }, [0]));
});


function errorHandling(res, item) {
  if (item === undefined) {
    res.sendStatus(404);
  } else {
    res.send(item);
  }
}

app.delete('/todos/:id', (req, res) => {
  const item = data.filter(e => {
    if (e.id === +req.params.id) {
      e.destroyed = true;
      data.splice(data.indexOf(e), 1);
      return e
    }
  })[0];
  errorHandling(res, item);
});

app.listen(3000);

const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

const data = [
  {
    completed: false,
    id: 1,
    text: 'Buy milk'
  },
  {
    'completed': false,
    'id': 2,
    'text': 'Make dinner'
  },
  {
    'completed': false,
    'id': 3,
    'text': 'Save the world'
  },
];

let counter = data.length;

app.get('/todos', function(req, res) {
  res.send(data);
});

app.get('/todos/:id', function (req, res) {
  res.send(data.filter(function(e) {
    if (parseInt(e.id) === parseInt(req.params.id)) {
      return e;
    } }));
});

app.post('/todos/', function (req, res) {
  counter++;
  let bit = {'completed' : false, 'id': counter, 'text': req.body.text};
  data.push(bit);
  res.send(data);
});

app.put('/todos/:id', function (req, res) {
  res.send(data.filter(function(e) {
    if (parseInt(e.id) === parseInt(req.params.id)) {
      e.completed = true;
      e.text = req.body.text;
    } }, [0]));
});

app.delete('/todos/:id', function (req, res) {
  try {
  res.send(data.filter(function(e) {
    if (parseInt(e.id) === parseInt(req.params.id)) {
      e.destroyed = true;
    }
  }, [0])); } catch (err) {
    res.send('404');
  }

});

app.listen(3000);

const express = require('express');
const app = express();
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

app.get('/todos', function(req, res) {
  res.send(data);
});

app.get('/todos/:id', function (req, res) {
  res.send(data.filter(function(e) {
    if (parseInt(e.id) === parseInt(req.params.id)) {
      return e;
    } }));
});



app.listen(3000);

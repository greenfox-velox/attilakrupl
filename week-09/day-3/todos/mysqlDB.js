const subFunctions = require('./subFunctions');
const mysql = require('mysql');
const con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma123',
  database: 'todos',
});

function getTodos(req, callback) {
  con.query('SELECT * from todos WHERE destroyed = 0;', (err, rows) => {
  subFunctions.errorHandling(err);
  callback(rows);
});
}
function getTodoByID(req, callback) {
  con.query('SELECT * from todos WHERE id = ?', req.params.id, (err, rows) => {
  subFunctions.errorHandling(err);
  callback(rows);
});
}
function postTodo(req, callback) {
  con.query('INSERT INTO todos SET ?', subFunctions.setNewTodo(req.body.text), (err, rows) => {
  subFunctions.errorHandling(err);
  callback(rows);
});
}
function modifyTodo(req, callback) {
  let text = subFunctions.defineBody(req.body).text;
  let complete = subFunctions.checkOrUncheck(req.body);
  let id = req.params.id;
  con.query('UPDATE todos SET text = ?, completed = ? Where ID = ?',
  [text, complete, id], (err, rows) => {
  subFunctions.errorHandling(err);
  callback(rows);
});
}
function deleteTodo(req, callback) {
  con.query('UPDATE todos SET destroyed = ? Where ID = ?', [1, req.params.id], (err, result) => {
    subFunctions.errorHandling(err);
    callback(result);
  });
}

module.exports.getTodos = getTodos;
module.exports.getTodoByID = getTodoByID;
module.exports.postTodo = postTodo;
module.exports.modifyTodo = modifyTodo;
module.exports.deleteTodo = deleteTodo;

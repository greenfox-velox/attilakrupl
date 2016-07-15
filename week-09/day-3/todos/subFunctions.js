function errorHandling(err) {
  if (err) {
    console.log(err.toString());
    return;
  }
}

function defineBody(body) {
  return JSON.parse(JSON.stringify(body))
}

function checkOrUncheck(body) {
  return defineBody(body).completed ? 1 : 0;
}

function setNewTodo(task) {
  return { completed : 0 , text:  task , destroyed : 0 }
}

module.exports.errorHandling = errorHandling;
module.exports.defineBody = defineBody;
module.exports.checkOrUncheck = checkOrUncheck;
module.exports.setNewTodo = setNewTodo;

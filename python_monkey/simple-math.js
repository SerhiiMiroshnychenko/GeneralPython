function add(a,b) {
  return a + b;
}

function sub(a,b) {
  return a - b;
}

// We'll define the exports object just like in Node.js / npm modules
module.exports = {
  add,
  sub,
}

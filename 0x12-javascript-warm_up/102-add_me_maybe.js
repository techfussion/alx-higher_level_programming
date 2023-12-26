#!/usr/bin/node

function addMeMaybe (num, fn) {
  fn(++num);
}

module.exports = { addMeMaybe };

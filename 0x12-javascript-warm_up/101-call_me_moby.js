#!/usr/bin/node

function callMeMoby (range, fn) {
  for (let i = 0; i < range; i++) {
    fn();
  }
}

module.exports = { callMeMoby };

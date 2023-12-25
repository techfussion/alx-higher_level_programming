#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const value1 = parseInt(process.argv[2]);
const value2 = parseInt(process.argv[3]);

add(value1, value2);

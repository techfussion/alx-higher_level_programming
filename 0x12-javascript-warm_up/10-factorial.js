#!/usr/bin/node
const myVar = parseInt(process.argv[2]);

function factorial (num) {
  if (num === 1) {
    return 1;
  }

  return num * factorial(num - 1);
}

if (myVar) {
  console.log(factorial(myVar));
} else {
  console.log('1');
}

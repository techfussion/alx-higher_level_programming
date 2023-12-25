#!/usr/bin/node
const myVar = parseInt(process.argv[2]);

if (myVar) {
  for (let i = 0; i < myVar; i++) {
    let sum = '';
    for (let j = 0; j < myVar; j++) {
      sum += 'X';
    }
    console.log(sum);
  }
} else {
  console.log('Missing size');
}

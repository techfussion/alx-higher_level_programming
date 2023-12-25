#!/usr/bin/node

const arr = process.argv.splice(2);

if (arr.length < 2) {
  console.log('0');
} else {
  let largest = arr[0];
  let secondLargest = -Infinity;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
      secondLargest = largest;
      largest = arr[i];
    } else if (arr[i] < largest && arr[i] > secondLargest) {
      secondLargest = arr[i];
    }
  }
  console.log(secondLargest);
}

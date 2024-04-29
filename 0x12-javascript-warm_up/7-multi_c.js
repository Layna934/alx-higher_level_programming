#!/usr/bin/node
const x = process.argv[2];
const number = parseInt(x);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  let itr = 0;
  while (itr < number) {
    console.log('C is fun');
    itr++;
  }
}

#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let row = 0;
  while (row < x) {
    let line = '';
    for (let col = 0; col < x; col++) {
      line += 'X';
    }
    console.log(line);
    row++;
  }
}

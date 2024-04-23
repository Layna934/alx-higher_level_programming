#!/usr/bin/node
console.log(isNaN(process.argv[2]) ? 'Not a Number' : `My Number: ${process.argv[2]}`);

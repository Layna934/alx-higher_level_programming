#!/usr/bin/node
const numArg = Math.floor(process.argv[2]);
console.log(isNaN(numArg) ? 'Not a Number' : `My Number: ${numArg}`);

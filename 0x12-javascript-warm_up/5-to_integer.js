#!/usr/bin/node
const numArg = Math.floor(Number(process.argv[2]));
console.log(isNaN(numArg) ? 'Not a Number' : `My Number: ${numArg}`);

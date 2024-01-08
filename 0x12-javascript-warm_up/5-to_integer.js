#!/usr/bin/node
//Script that prints My number: <first argument converted in integer>

const MyNum = parseInt(process.argv[2]);
if (isNaN(MyNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${MyNum}`);
}

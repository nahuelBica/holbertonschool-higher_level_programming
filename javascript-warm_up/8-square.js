#!/usr/bin/node
const num = Number(process.argv[2]);
let line = '';

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < num; j++) {
    line += 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(line);
  }
}

#!/usr/bin/node
const langs = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let mesage = langs[0];

for (let i = 1; i < langs.length; i++) {
  mesage += '\n' + langs[i];
}

console.log(mesage);

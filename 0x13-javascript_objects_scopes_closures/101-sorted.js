#!/usr/bin/node
const dict = require('./101-data').dict;

const newdict = {};
for (const key in dict) {
  if (Object.hasOwnProperty.call(dict, key)) {
    if (Object.hasOwnProperty.call(newdict, dict[key])) {
      newdict[dict[key]].push(key);
    } else {
      const list = [key];
      newdict[dict[key]] = list;
    }
  }
}
console.log(newdict);

#!/usr/bin/node
const list = require('./100-data').list;

const newlist = list.map((e, idx) => (e * idx));
console.log(list);
console.log(newlist);

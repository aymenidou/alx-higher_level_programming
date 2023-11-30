#!/usr/bin/node
const fs = require('fs');

const data1 = fs.readFileSync("fileA", "utf8")
console.log(data1);
const data2 = fs.readFileSync("fileB", "utf8")
console.log(data2);
const data3 = fs.writeFileSync("fileC", data1 + "\n" + data2, "utf8")

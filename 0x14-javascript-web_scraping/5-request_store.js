#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const filename = process.argv[3];
    fs.writeFileSync(filename, body, 'utf8');
  }
});

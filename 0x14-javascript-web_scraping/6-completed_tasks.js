#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const users = {};
    const resJson = JSON.parse(body);
    resJson.forEach(element => {
      if (element.userId in users && element.completed === true) {
        users[element.userId] += 1;
      } else if (!(element.userId in users) && element.completed === true) {
        users[element.userId] = 1;
      }
    });
    console.log(users);
  }
});

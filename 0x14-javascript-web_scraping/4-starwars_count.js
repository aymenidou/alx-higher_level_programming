#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const resJson = JSON.parse(body).results;
    let count = 0;
    resJson.forEach((movie) => {
      if (movie.characters.find((char) =>
        char.includes('/people/18/'))
      ) { count++; }
    }
    );
    console.log(count);
  }
});

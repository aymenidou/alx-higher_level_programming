#!/usr/bin/node
const request = require('request');
const urlFilm = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
// const urlPeople = 'https://swapi-api.alx-tools.com/api/people/';

request(urlFilm, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    // console.log(characters);
    // const people = {}
    for (let index = 0; index < characters.length; index++) {
      const element = characters[index];
      request(element, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          // JSON.parse(body).results.forEach(people => {
          console.log(JSON.parse(body).name);
          // for (let index = 0; index < characters.length; index++) {
          //   const element = characters[index];
          //   if (element == people.url) {
          //     console.log(people.name);
          //   }
          // }

          // });
        }
      });
    }
  }
});

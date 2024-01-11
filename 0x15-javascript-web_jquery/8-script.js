#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
  if (status === 'success') {
    data.results.forEach(i => {
      $('UL#list_movies').append(`<li>${i.title}</li>`);
    });
  }
});

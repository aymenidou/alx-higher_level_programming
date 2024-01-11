#!/usr/bin/node
$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data, status) => {
    if (status === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});

#!/usr/bin/node
const $ = window.$;
$('div#toggle_header').click(() => {
  $('header').toggleClass('green red');
});

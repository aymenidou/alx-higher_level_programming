#!/usr/bin/node
const $ = window.$;
$('div#red_header').click(() => {
  $('header').css('color', '#FF0000');
});

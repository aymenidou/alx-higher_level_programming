#!/usr/bin/node
const $ = window.$;
$('div#update_header').click(function (e) {
  $('header').text('New Header!!!');
});

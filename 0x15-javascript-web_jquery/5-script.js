#!/usr/bin/node
const $ = window.$;
$('div#add_item').click(function (e) {
  $('ul.my_list').append('<li>Item</li>');
});

#!/usr/bin/node
$('div#add_item').click(function (e) { 
  $('ul.my_list').append('<li>Item</li>')
});

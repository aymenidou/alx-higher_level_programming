#!/usr/bin/node
const URL = 'https://hellosalut.stefanbohacek.dev/';
const $ = window.$;
function SayHello (lang) {
  $.get(`${URL}?lang=${lang}`, (data, status) => {
    if (status === 'success' && lang) {
      $('DIV#hello').text(data.hello);
    }
  });
}

$(document).ready(function () {
  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();
    SayHello(lang);
  });
  $('#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === 13) {
      const lang = $('#language_code').val();
      SayHello(lang);
    }
  });
});

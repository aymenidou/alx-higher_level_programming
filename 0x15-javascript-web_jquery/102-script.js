
const URL = 'https://hellosalut.stefanbohacek.dev/';

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
});

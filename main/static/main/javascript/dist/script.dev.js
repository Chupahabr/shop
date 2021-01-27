"use strict";

$(document).ready(function () {
  // CSRF code
  var csrftoken = getCookie('csrftoken');
  $.ajaxSetup({
    crossDomain: false,
    // obviates need for sameOrigin test
    beforeSend: function beforeSend(xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
  $('#buscket').on('click', function (e) {
    // e.preventDefault();
    // var $this = $(this),
    // data = $this.data();
    // $this.hide();
    console.log('LF');
    $.ajax({
      url: '/buscket-insert',
      method: 'POST',
      data: {
        'busk': $(this).val()
      },
      success: function success(d) {
        console.log(d);
      },
      error: function error(d) {
        console.log(d);
      }
    });
  });
});

function getCookie(name) {
  var cookieValue = null;
  var i = 0;

  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');

    for (i; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]); // Does this cookie string begin with the name we want?

      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }

  return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
} // $(document).ready(function() {
//       $('#buscket').click(function(e) {
//         // Stop form from sending request to server
//         e.preventDefault();
//         var btn = $(this);
//         console.log('click');
//         $.ajax({
//             method: "POST",
//             url: "/buscket-insert",
//             dataType: "json",
//             data: {
//               "name": btn.val(),
//               'input': $('input').val()
//             },
//             success: function(data) {
//               console.log(data);
//             },
//             error: function(er) {
//               console.log(er);
//             }
//         });
//       })
// });
$(document).ready(function() {
    $('#buscket').click(function(e) {
      // Stop form from sending request to server
      e.preventDefault();
  
      var btn = $(this);
      console.log('click');
      $.ajax({
        method: "POST",
        url: "/buscket-insert",
        dataType: "json",
        data: {
          "name": btn.val(),
          'input': $('input').val()
        },
        success: function(data) {
          console.log(data);
        },
        error: function(er) {
          console.log(er);
        }
      });
    })
});
$(document).ready(function() {
    // CSRF code
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
        }
    });
    let tf = false;
    $('#heart').on('click', function(e) {
        if ($('#heart .bi-heart-fill').hasClass('d-none')) {
            $('#heart .bi-heart').removeClass('d-inline');
            $('#heart .bi-heart').addClass('d-none');
            $('#heart .bi-heart-fill').removeClass('d-none');
            $('#heart .bi-heart-fill').addClass('d-inline');
        }
        else{
            $('#heart .bi-heart').removeClass('d-none');
            $('#heart .bi-heart').addClass('d-inlinte');
            $('#heart .bi-heart-fill').removeClass('d-inline');
            $('#heart .bi-heart-fill').addClass('d-none');
        }
        $.ajax({
            url: '/fav-ins',
            method: 'POST',
            data: {
                'fav': $(this).val(),
            },
            success: function(d) {
                console.log(d);
            },
            error: function(d) {
                console.log(d);
            }
        });
    });
    $('#buscket').on('click', function(e) {
        if ($('#buscket').hasClass('btn-danger')) {
            $('#buscket').removeClass('btn-danger');
            $('#buscket').addClass('btn-success');
        }
        else if($('#buscket').hasClass('btn-success')){
            $('#buscket').removeClass('btn-success');
            $('#buscket').addClass('btn-danger');
        }
        $.ajax({
            url: '/bascket-insert',
            method: 'POST',
            data: {
                'bask': $(this).val(),
            },
            success: function(d) {
                console.log(d);
            },
            error: function(d) {
                console.log(d);
            }
        });
    });

});

function delete_bask(e){
    sel = $('.select_count[name='+e+']');
    $.ajax({
        url: '/bascket-delete',
        method: 'POST',
        data: {
            'prod': e,
        },
        success: function(d) {
            $('.price').val(d);
            $('#prod-'+e).remove()
        },
        error: function(d) {
            console.log(d);
        }
    });
}
function change_sel(e){
    sel = $('.select_count[name='+e+']');
    $.ajax({
        url: '/bascket-count-update',
        method: 'POST',
        data: {
            'count': sel.val(),
            'prod': e,
        },
        success: function(d) {
            $('.price').val(d);
            console.log(d);
        },
        error: function(d) {
            console.log(d);
        }
    });
}
$('#id_delivery_method').on('change', function () {
    sel = $('#id_delivery_method');
    if (sel.val() == 'D'){
        $('#append_input_form').removeClass('d-none');
    }
    else if (sel.val() == 'P'){
        $('#append_input_form').addClass('d-none');
    }
});
function getCookie(name) {
    var cookieValue = null;
    var i = 0;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
  return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

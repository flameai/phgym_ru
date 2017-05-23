var validator;

$(function(){
  setCSRFAjaxHeader();

  $('.form_interview').on('change',function() {
    if( $(this).is(':checked') ) {
      $('.interview').fadeIn();
    } else {
      $('.interview').fadeOut();
    }
  });

  validator = $('#form').validate();

  $('#form_submit').on('click', sendform);

  var link = $('nav div').filter(function(){
    return $(this).children("a").attr("href") == "/" + location.pathname.split("/")[1] + "/"
  });
  if(link.length) {
    link.addClass('active')
  } else {
    $("nav div.address-wraper").last().addClass("active");
  }

  $('.carousel').carousel({
    interval: 6000
  });

  $(".navigation").change(function(){
    if($(this).val().indexOf("http://") != -1) {
      window.open($(this).val(),'_blank');
    } else {
      document.location.href = $(this).val();
    }
  });

    $(".carousel-slick").slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            infinite: true,
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,
          }
        }]
    })

    $('.to_about').on('click', function(){
        $('body').scrollTop(1285);
        return false;
    });

});

$(document).ready(function(){
    var url = location.pathname.split('/')[1];
    if(url && url != 'news' && url != 'pages') {
      if ($(".navigation option[value='/"+url+"']").length > 0)
        $('.navigation').val('/'+url);
    }
});

function sendData(url, data) {
    return $.ajax({
      type: 'post',
      url: url,
      data: data,
    })
}

function sendform() {
  if(validator.form()) {
    var subject = $('#formsubject').val();
    var url = $('#form').attr('action'),
        data = {};
    switch(subject) {
      case "ЗАКАЗ АБОНЕМЕНТА":
        data = {
          Name: $('#formName').val(),
          Tel: $('#formTel').val(),
          subject: subject
        }
        sendData(url,data).done(() => {
          // ga & yandex for abonement
          yaCounter29959819.reachGoal('order'); 
          // ga('send', 'event', "card", "success");
          
          $('#form_modal').arcticmodal({
            afterOpen: function() {
              setTimeout(
                function() {
                  $.arcticmodal('close');
                  window.location = window.location.href.split("abonement")[0];
                },
              2000 )
            }
          });
        })
      case "ЗАКАЗ ЗВОНКА С САЙТА":                // call
        data = {
          Name: $('#formName').val(),
          Tel: $('#formTel').val(),
          subject: subject
        }
        sendData(url,data).done(() => {
          // ga & yandex for call
          yaCounter29959819.reachGoal('callorder');
          // ga('send', 'event', "callback", "success");
          $('#form_modal').arcticmodal({
            afterOpen: function() {
              setTimeout(
                function() {
                  $.arcticmodal('close');
                  window.location = window.location.href.split("call")[0];
                }
              , 2000 )
            }
          });
        })
        break;
      case "ЗАКАЗ БЕСПЛАТНОГО ЗАНЯТИЯ С САЙТА":   // entry
       data = {
         Name: $('#formName').val(),
         Tel: $('#formTel').val(),
         Email: $('#formEmail').val(),
         Club: $('#formClub').val(),
         subject: subject,
         Interview: $('#inter').val(),
         origin: [],
         service: [],
         target: [],
       }
       if(data.Interview == "on") {
         $('[name=origin]:checked').each(function(){
           data['origin'].push($(this).val());
         });
         $('[name=service]:checked').each(function(){
           data['service'].push($(this).val());
         })
         $('[name=target]:checked').each(function(){
           data['target'].push($(this).val());
         })
         data['parametr'] = $('[name=parametr]:checked').val();
       }
       sendData(url,data).done(() => {
         // ga & yandex for entry
        //  yaCounter38885450.reachGoal('freetrain_success');
        //  ga('send', 'event', "freetrain", "success");
         $('#form_modal').arcticmodal({
            afterOpen: function() {
              setTimeout(
                function() {
                  $.arcticmodal('close');
                  window.location = window.location.href.split("entry")[0];
                }
              , 2000 )
            }
         });
       })
       break;
    }

  }
  return false;
}

function setCSRFAjaxHeader () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

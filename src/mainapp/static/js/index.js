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

$(document).ready(function() {
  var shedule_modal = $(document).find("#timetable-modal")[0]

  var getId = function(element) {
    var ids = element.id.split('-')
    return ids[ids.length - 1]
  } 

  var prepareModal = function(id) {
    var data = {}
    $(".entries-data").find("#entry-data-" + id).children().each(function() {
      var parts = this.classList[0].split("-")
      var last = parts[parts.length - 1]
      if(last == "image") {
        data[last] = (this.textContent[this.textContent.length - 1] === '/') ? "" : this.textContent
      } else {
        data[last] = this.textContent
      }
    })

    $(shedule_modal).find("#timetable-modal-content").text(data.content)

    $(shedule_modal).find("#timetable-modal-description").text(data.description)

    $(shedule_modal).find(".timetable-modal-weekday").each(function() {
      this.textContent = data.weekday
    })

    $(shedule_modal).find(".timetable-modal-duration").each(function() {
      this.textContent = data.time + " (" + data.duration + " минут)"
    })

    if(data.image) {
      var img = $(shedule_modal).find("#timetable-modal-image")
      $(img).attr("src", data.image)
      $(img).removeClass("hide")
      $(shedule_modal).find("#timetable-modal-description").parent().removeClass("wide")
    } else {
      $(shedule_modal).find("#timetable-modal-image").addClass("hide")
      $(shedule_modal).find("#timetable-modal-description").parent().addClass("wide")
    }
  }

  $(".timetable *[id*='entry-']").click(function() {
    prepareModal(getId(this))
    $(shedule_modal).modal('show')
  })
  $(".schedule-table *[id*='entry-mobile-'").click(function() {
    if(this.textContent) {
      prepareModal(getId(this))
      $(shedule_modal).modal('show')
    }
  })
})

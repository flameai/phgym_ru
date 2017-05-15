var app = {
    page: ko.observable('auth'),
    currentClub: ko.observable(),
    club: ko.observable(),
    clubs: ko.observableArray(),

    getClubs: function(done) {
      $.ajax({
        // url: 'https://api.wge.ru/sportclub/hs/fitnes_mob/clubs',
        url: '/static/plastic/clubs.json',
        dataType: 'json',
        success: function(data) {
          if(data.status == "ok") {
            app.clubs(data.clubs);
            done && done();
          } else {
            alert('Произошла ошибка. Повторите попытку позже.');
          }
        },
        error: function(data) {
          alert('Произошла ошибка. Повторите попытку позже.');
        }
      });
    },
    sendEmail: function(email) {
     $.ajax({
       type: "post",
       url: '/shop/send_register_email',
       data: {
         email: email
       }
     });
   },
  buyItem: function(a) {
    m_payment.item_kod(a.item_kod);
    m_payment.order_type(a.type);
    m_payment.club(app.club());
    app.clubs().forEach(function(cl){
      cl.goods.forEach(function(go){
        if (go.item_kod === m_payment.item_kod())
          m_payment.club_code(cl.club_code);
      })
    })

    app.page('phone');
  },
   startPayment: function() {
     data = ko.mapping.toJS(m_payment);
     $.post("/shop/payment/",data,function(response){
       var form = $(response).find('form');
       $('div#hiddenForm').append(form)
       $('div#hiddenForm').find('form').submit();
     });
   },
   getOferta: function(name) {
     $.ajax({
       type: 'get',
       url: '/oferta/' + name + "/"
     })
     .done(function(response){
       $('.oferta_context').html(response)
     })
     .fail(function(response){
       $('.oferta_context').html("Оферта не найдена")
     })
   }
}

app.currentClub = ko.computed(function(){
  return app.clubs().find(function(club){
    return club.club == app.club();
  });
});

app.page.subscribe(function(newValue){
  if(newValue == "registration") {
    app.getOferta('first')
  }
});

$(document).ready(function() {
  setCSRFAjaxHeader();
  app.getClubs(function() {
    app.page('site');
    ko.applyBindings(app);
  });
});


function setCSRFAjaxHeader () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
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
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
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

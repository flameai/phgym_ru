m_registration = {
  fio: ko.observable(""),
  email: ko.observable(""),
  oferta: ko.observable(false)
}

m_registration.registration = function() {
  $.ajax({
    type: "POST",
    url: "https://api.wge.ru/sportclub/hs/fitnes_mob/client_new",
    // url: '/static/plastic/client_new.json',
    data: JSON.stringify({
      "fio": m_registration.fio(),
      "email": m_registration.email(),
      "phone": m_auth.phone(),
      "passport": "",
      "birth": "",
      "club": ""
    }),
    success: function(data) {
      if(data.status == "ok") {
        app.sendEmail(m_registration.email());
        m_payment.user_id(data.user_id);
        m_payment.phone(m_auth.phone())
        m_payment.email(m_registration.email());
        app.startPayment();
      }
    },
    error: function(err) {
      console.log(err);
    },
    // contentType: 'application/json; charset=utf-8',
    dataType: 'json'
  });
}

m_registration.registerValidate = ko.computed(function(){
    if(m_registration.fio() && m_registration.email() && m_registration.oferta()) {
      return true;
    }
    return false;
});

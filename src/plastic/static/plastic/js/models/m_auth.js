m_auth = {
  phone: ko.observable("7"),
  pin: ko.observable(""),

  in_progress: ko.observable(false),
  error: ko.observable(false),
}

m_auth.sendPhone = function() {
  if(!this.in_progress()) {
    this.sendSMS();
  }
  this.in_progress(true);
  app.page('sms');
}

m_auth.sendSMS = function() {
  $.ajax({
    type: 'post',
    url: '/shop/send_sms',
    data: {
      phone: this.phone(),
    }
  })
}

m_auth.authorization = function() {
  $.ajax({
    type: "get",
    url: "/shop/check_pin",
    data: {
      "phone": m_auth.phone(),
      "pin": m_auth.pin(),
    },
    success: function(data) {
      if(data.status !== "error") {
        $.ajax({
          type: "POST",
          url: "https://api.wge.ru/sportclub/hs/fitnes_mob/client_check",
          // url: '/static/plastic/client_check.json',
          data: JSON.stringify({"phone": m_auth.phone()}),
          success: function(data) {
            if(data.status == "exist") {
                m_payment.user_id(data.user_id);
                m_payment.email(data.email);
                m_payment.phone(m_auth.phone());
                m_auth.in_progress(false);
                app.startPayment();
            } else if(data.status == "new") {
                m_auth.in_progress(false);
                app.page('registration');
            }
          },
          error: function(err) {
            console.log(err)
          },
          contentType: 'application/json; charset=utf-8',
          dataType: 'json'
        });
      } else {
        m_auth.error(true);
        app.page('sms');
      }
    },
    error: function(err) {
      console.log(err)
    }
  });
}

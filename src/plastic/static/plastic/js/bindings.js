ko.bindingHandlers.masked = {
    init: function(element, valueAccessor, allBindingsAccessor) {
        var mask = allBindingsAccessor().mask || {};
        $(element).mask(mask);
        ko.utils.registerEventHandler(element, 'change', function() {
            var observable = valueAccessor();
            observable($(element).val());
        });
    },
    update: function (element, valueAccessor) {
        var value = ko.utils.unwrapObservable(valueAccessor());
        $(element).val(value);
    }
};

ko.bindingHandlers.datepicker = {
  init: function(element, valueAccessor, allBindingsAccessor) {
    $(element).pickadate({
      selectMonths: true,
      selectYears: 150,
      format: 'dd.mm.yyyy',
      // перенести в отдельный файл перевода
      labelMonthNext: 'Следующий месяц',
      labelMonthPrev: 'Предыдущий месяц',

      labelMonthSelect: 'Выбрать месяц',
      labelYearSelect: 'Выбрать год',

      monthsFull: [ 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь' ],
      monthsShort: [ 'Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек' ],
      weekdaysFull: [ 'Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота' ],
      weekdaysShort: [ 'Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб' ],
      weekdaysLetter: [ 'В', 'П', 'В', 'С', 'Ч', 'П', 'С' ],

      close: '',
      today: '',
      clear: '',
      onClose: function() {
        $('.picker').blur();
      },
      closeOnSelect: true,

      firstDay: true
    });

    ko.utils.registerEventHandler(element,'change', function() {
      var observable = valueAccessor();
      observable($(element).val());
    })
  },
  update: function(element, valueAccessor) {
    var value = ko.utils.unwrapObservable(valueAccessor());
    $(element).val(value);
  }
}

ko.bindingHandlers.materialselect = {
  init: function(element, valueAccessor, allBindingsAccessor) {
    ko.bindingHandlers.options.init(element);
    setTimeout(function(){
      $(element).material_select();
    },0);
  },
  update: function (element, valueAccessor, allBindingsAccessor, viewModel) {
    allBindingsAccessor.optionsText = allBindingsAccessor.optionsText || function(item) {return window.MyApplication.GetText(item)};
    allBindingsAccessor.optionsValue = allBindingsAccessor.optionsValue || 'dataId';
    ko.bindingHandlers.options.update(element, valueAccessor, allBindingsAccessor);
  }
}

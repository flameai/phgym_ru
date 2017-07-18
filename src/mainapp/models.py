# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Max
from django import forms
from datetime import date, datetime
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils.safestring import mark_safe

FORM_CHOICES = (
    (1, u"Бесплатный фитнес-день"),
    (2, u"Заказать звонок"),
    (3, u"Заказать абонемент")
)

class FormRequest(models.Model):
    formname = models.IntegerField(choices=FORM_CHOICES, verbose_name=u'Форма')
    content = models.TextField(u'Текст запроса')
    daterequest = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата заявки')

    def __str__(self):
        return u"%s" % self.formname

    def __unicode__(self):
        return u"%s" % self.formname

    class Meta:
        verbose_name = u'заявка с форм'
        verbose_name_plural = u'заявки с форм'


class Club(models.Model):
    address = models.CharField(verbose_name=u"Адрес",max_length=200)
    phone = models.CharField(verbose_name=u"Телефоны",max_length=200)
    email = models.CharField(verbose_name=u"E-mail для контактов",max_length=200)
    emails_send = models.CharField(verbose_name=u'E-майл для заявок', help_text=u'Можно указывать несколько значений через запятую.', max_length=200, default='')
    worktime = models.CharField(verbose_name=u"Время работы",max_length=200)
    slug = models.SlugField(verbose_name=u"Слаг", default="")
    callibri = models.CharField(verbose_name=u"Callibri", max_length=50, default="", blank=True)
    lat = models.FloatField(verbose_name=u'широта', default=0.,)
    lon = models.FloatField(verbose_name=u'долгота', default=0.,)
    order = models.PositiveIntegerField(default=0)
    code = models.CharField(verbose_name=u'код в системе 1С', max_length=200,
                            unique=True, null=True, blank=True,
                            help_text=u"Должен совпадать с кодом из API https://api.wge.ru/sportclub/hs/fitnes_mob/clubs")
    cash_register = models.ForeignKey('yandex_cash_register.CashRegister',
                                      null=True, blank=True)

    def __str__(self):
        return self.address

    def __unicode__(self):
        return self.address

    class Meta:
        verbose_name = u"клуб"
        verbose_name_plural = u"клубы"


class News(models.Model):
    title = models.CharField(u'заголовок',max_length=65)
    slug = models.SlugField(u'слаг', max_length=200, unique=True, default="")
    date = models.DateTimeField(u'дата',default=datetime.now)
    image = models.ImageField(u'миниатюра',default="")
    short_text = models.TextField(u'краткий текст новости',default="",max_length=210, help_text="Максимальная длина анонса - 210 символов. Все остальные символы будут удалены.")
    full_text = RichTextUploadingField(u'полный текст новости',default="",)
    hidden = models.BooleanField(verbose_name=u'скрыть', default=False)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'


class Stock(models.Model):
    title = models.CharField(verbose_name=u'заголовок', max_length=65)
    slug = models.SlugField(u'слаг', max_length=200, unique=True, default="")
    date = models.DateField(u'дата', default=date.today)
    image = models.ImageField(u'миниатюра',default="")
    full_text = RichTextUploadingField(verbose_name=u'полный текст')
    show_button = models.BooleanField(u'отображать кнопку', default=False)
    text_button = models.CharField(u'текст на кнопке', max_length=200, default="", blank=True, null=True)
    url_button = models.URLField(u'ссылка кнопки', default='', blank=True, null=True )
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, verbose_name=u'клуб')
    order = models.PositiveIntegerField(verbose_name=u'сортировка', default=0)
    hidden = models.BooleanField(verbose_name=u'скрыть', default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            try:
                stocks = Stock.objects.all()
                for stock in stocks:
                    stock.order += 1
                    stock.save()
                self.order = 0
            except:
                pass
        super(Stock, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'акция'
        verbose_name_plural = u'акции'
        ordering = ('order',)


class Program(models.Model):
    title = models.CharField(verbose_name=u'название',max_length=255)
    slug = models.SlugField(u'слаг', max_length=200, unique=True, default="")
    date = models.DateField(u'дата', default=date.today)
    image = models.ImageField(verbose_name=u'Изображение')
    full_text = RichTextUploadingField(verbose_name=u'Подробное содержание')
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, verbose_name=u'клуб')

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'программа'
        verbose_name_plural = u'программы'


class Gym(models.Model):
    title = models.CharField(verbose_name=u'Название',max_length=255)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None, verbose_name=u"Клуб",)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'зал'
        verbose_name_plural = u'залы'

class WeekDay(models.Model):
    DAY_OF_WEEK = (
        (1,u"Понедельник"),
        (2,u"Вторник"),
        (3,u"Среда"),
        (4,u"Четверг"),
        (5,u"Пятница"),
        (6,u"Суббота"),
        (7,u"Воскресенье"),
    )
    day = models.IntegerField(verbose_name=u"День недели",choices=DAY_OF_WEEK)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None, verbose_name=u"зал",)

    def __str__(self):
        day_of_week = {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
            7: "Воскресенье"
        }
        return day_of_week[self.day]

    class Meta:
        unique_together = ('gym', 'day')
        verbose_name = u'расписание'
        verbose_name_plural = u'расписания'


class EntryTemplate(models.Model):
    name = models.CharField(verbose_name=u"название", max_length=200,)
    description = RichTextField(verbose_name=u"описание", config_name='links_only', blank=True, null=True)
    image = models.ImageField(verbose_name=u"изображение", blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'шаблон занятия'
        verbose_name_plural = u'шаблоны занятий'


class Entry(models.Model):
    TIME_CHOICES = (
        (71,u"07:00"),  (72,u"07:15"),  (73,u"07:30"),  (74,u"07:45"),
        (81,u"08:00"),  (82,u"08:15"),  (83,u"08:30"),  (84,u"08:45"),
        (91,u"09:00"),  (92,u"09:15"),  (93,u"09:30"),  (94,u"09:45"),
        (101,u"10:00"), (102,u"10:15"), (103,u"10:30"), (104,u"10:45"),
        (111,u"11:00"), (112,u"11:15"), (113,u"11:30"), (114,u"11:45"),
        (121,u"12:00"), (122,u"12:15"), (123,u"12:30"), (124,u"12:45"),
        (131,u"13:00"), (132,u"13:15"), (133,u"13:30"), (134,u"13:45"),
        (141,u"14:00"), (142,u"14:15"), (143,u"14:30"), (144,u"14:45"),
        (151,u"15:00"), (152,u"15:15"), (153,u"15:30"), (154,u"15:45"),
        (161,u"16:00"), (162,u"16:15"), (163,u"16:30"), (164,u"16:45"),
        (171,u"17:00"), (172,u"17:15"), (173,u"17:30"), (174,u"17:45"),
        (181,u"18:00"), (182,u"18:15"), (183,u"18:30"), (184,u"18:45"),
        (191,u"19:00"), (192,u"19:15"), (193,u"19:30"), (194,u"19:45"),
        (201,u"20:00"), (202,u"20:15"), (203,u"20:30"), (204,u"20:45"),
        (211,u"21:00"), (212,u"21:15"), (213,u"21:30"), (214,u"21:45"),
        (221,u"22:00"), (222,u"22:15"), (223,u"22:30"), (224,u"22:45"),
    )

    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE, default=None,)
    content = models.ForeignKey(EntryTemplate, verbose_name=u"Занятие", max_length=200,)
    time = models.IntegerField(verbose_name=u"время начала", choices=TIME_CHOICES,)
    duration = models.IntegerField(verbose_name=u"длительность", help_text=u"целое число в минутах")

    def __str__(self):
        return "%s" % self.content

    def __unicode__(self):
        return "%s" % self.content

    class Meta:
        unique_together = ('weekday','time')
        verbose_name = u'занятие'
        verbose_name_plural = u'занятия'


class Slider(models.Model):
    image = models.ImageField(verbose_name=u'Изображение')
    title_internal = models.CharField(verbose_name=u'Название', max_length=200, help_text=u"Отображается только в адм.части")
    button_url = models.URLField(verbose_name=u'Ссылка', blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = u'слайдер'
        verbose_name_plural = u'слайдеры'

    def __str__(self):
        return "%s" % self.title_internal

    def __unicode__(self):
        return "%s" % self.title_internal


class Form(models.Model):
    FORM_CHOICES = (
        # (1, u"Бесплатный фитнес-день"),
        (2, u"Заказать звонок"),
        (3, u"Заказать абонемент")
    )
    form = models.IntegerField(verbose_name=u"Форма", choices=FORM_CHOICES,)
    title = models.CharField(verbose_name=u"заголовок", max_length=200, default="")
    club = models.ForeignKey(Club, null=True, blank=True, on_delete=models.CASCADE, verbose_name=u'Клуб')
    context = RichTextUploadingField()

    def get_link(self):
        if self.form == 1:
            return mark_safe(u'<a href="/%s/entry/">Посмотреть</a>' % self.club.slug)
        elif self.form == 2:
            return mark_safe(u'<a href="/%s/call/">Посмотреть</a>' % self.club.slug)
        elif self.form == 3:
            return mark_safe(u'<a href="/%s/abonement/">Посмотреть</a>' % self.club.slug)
    get_link.short_description = u'Ccылка'
    link = property(get_link)

    def __str__(self):
        return u"%s" % self.title

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = u'Форма'
        verbose_name_plural = u'Формы'
        unique_together = ('form', 'club')


class Page(models.Model):
    title = models.CharField(u'заголовок', max_length=200)
    slug = models.SlugField(u'слаг', max_length=200, unique=True)
    content = RichTextUploadingField(u'Контент')
    url = models.URLField(u'URL', default="", blank=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return u"%s" % self.title

    def __unicode__(self):
        return u"%s" % self.title

    def save(self, *args, **kwargs):
        self.url = settings.PAGES_URL + self.slug + "/"
        super(Page, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'страница'
        verbose_name_plural = u'страницы'


class StaticPage(models.Model):
    title = models.CharField(u'название', max_length=200, default='')
    club = models.OneToOneField(Club, on_delete=models.CASCADE, default=None, blank=True, null=True,)
    context = RichTextUploadingField(verbose_name=u'содержание')

    class Meta:
        verbose_name = u'статическая страница'
        verbose_name_plural = u'статические страницы'

class FitnesZone(models.Model):
    title = models.CharField(u'название', max_length=200, default='')
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, verbose_name=u'клуб')
    image = models.ImageField(u'рисунок')
    link = models.URLField(u'ссылка')

    def __str__(self):
        return u"%s" % self.title

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = u'фитнес-зона'
        verbose_name_plural = u'фитнес-зоны'


class EditTextField(models.Model):
    PAGE_CHOICES = (
        (1, "Программы"),
    )

    club = models.ForeignKey(Club, verbose_name=u'клуб', on_delete=models.CASCADE, )
    page = models.IntegerField(u'страница', choices=PAGE_CHOICES, default=1)
    context = RichTextUploadingField(u'содержание')

    def __str__(self):
        return u'%s' % self.club

    def __unicode__(self):
        return u'%s' % self.club

    class Meta:
        unique_together = ('club','page')
        verbose_name = u'текстовый блок'
        verbose_name_plural = u'текстовые блоки'


class YouTubeChannel(models.Model):
    club = models.OneToOneField(Club, verbose_name=u'клуб', on_delete=models.CASCADE, null=True, blank=True)
    html = models.TextField(
        help_text=u"""1. На странице <a href='https://elfsight.com/youtube-channel-plugin-yottie/jquery/#demo'>ссылка</a> настройте виджет.<br>
                      2. В последнем пункте Get Code скопируйте полученный код виджета (2-ое поле).<br>
                      3. Вставьте этот код в это поле."""
    )

    def __str__(self):
        if self.club:
            return u'YouTube канал клуба %s' % self.club
        else:
            return u'YouTube канал по умолчанию'

    def __unicode__(self):
        if self.club:
            return u'YouTube канал клуба %s' % self.club
        else:
            return u'YouTube канал по умолчанию'


    def save(self, *args, **kwargs):
        if u"data-yt-key" not in self.html:
            new = u'%s%s%s%s%s' % (self.html[:13], 'data-yt-key="', settings.YT_API_KEY, '" ', self.html[13:])
            self.html = new
        super(YouTubeChannel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'YouTube канал'
        verbose_name_plural = u'YouTube каналы'


class MainInfo(models.Model):
    phone = models.CharField(verbose_name=u"телефон", max_length=200)

    def __str__(self):
        return u'Основная информация'

    def __unicode__(self):
        return u'Основная информация'

    class Meta:
        verbose_name = u'основная информация'
        verbose_name_plural = u'основная информация'

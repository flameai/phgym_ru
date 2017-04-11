# -*- coding: utf-8 -*-
from django.db import models
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
    email = models.CharField(verbose_name=u"E-mail",max_length=200)
    worktime = models.CharField(verbose_name=u"Время работы",max_length=200)
    slug = models.SlugField(verbose_name=u"Слаг", default="")
    callibri = models.CharField(verbose_name=u"Callibri", max_length=50, default="", blank=True)
    lat = models.FloatField(verbose_name=u'широта', default=0.,)
    lon = models.FloatField(verbose_name=u'долгота', default=0.,)
    order = models.PositiveIntegerField(default=0)

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

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'акция'
        verbose_name_plural = u'акции'


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
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None, verbose_name=u"Клуб",)

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
        verbose_name_plural = u'расписание'

class Entry(models.Model):
    TIME_CHOICES = (
        (1,u"08:00 - 09:00"),
        (2,u"09:00 - 10:00"),
        (3,u"10:00 - 11:00"),
        (4,u"11:00 - 12:00"),
        (5,u"12:00 - 13:00"),
        (6,u"13:00 - 14:00"),
        (7,u"14:00 - 15:00"),
        (8,u"15:00 - 16:00"),
        (9,u"16:00 - 17:00"),
        (10,u"17:00 - 18:00"),
        (11,u"18:00 - 19:00"),
        (12,u"19:00 - 20:00"),
        (13,u"20:00 - 21:00"),
    )
    PROGRAM_CHOICES = (
        (1,u"TOP-FITNESS"),
        (2,u"Studio"),
        (3,u"Прочее"),
    )
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE, default=None,)
    time = models.IntegerField(verbose_name=u"Время",choices=TIME_CHOICES,)
    content = models.CharField(verbose_name=u"Занятие",max_length=200,)
    program = models.IntegerField(verbose_name=u"Программа",choices=PROGRAM_CHOICES,)


    class Meta:
        unique_together = ('weekday','time')
        verbose_name = u'занятие'
        verbose_name_plural = u'занятия'

class Slider(models.Model):
    image = models.ImageField(verbose_name=u'Рисунок')
    title = models.CharField(verbose_name=u'Заголовок', max_length=200)
    subtitle = models.CharField(verbose_name=u'Подзаголовок', max_length=200, default="")
    context = RichTextField(verbose_name=u'Текст')
    button_url = models.URLField(verbose_name=u'Ссылка кнопки', blank=True)
    button_text = models.CharField(verbose_name=u'Текст на кнопке', max_length=100, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = u'слайдер'
        verbose_name_plural = u'слайдеры'

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "%s" % self.title

class Form(models.Model):
    FORM_CHOICES = (
        (1, u"Бесплатный фитнес-день"),
        (2, u"Заказать звонок"),
        (3, u"Заказать абонемент")
    )
    form = models.IntegerField(verbose_name=u"Форма", choices=FORM_CHOICES,)
    title = models.CharField(verbose_name=u"заголовок", max_length=200, default="")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name=u'Клуб')
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
        return u'YouTube канал клуба %s' % self.club

    def __unicode__(self):
        return u'YouTube канал клуба %s' % self.club

    def save(self, *args, **kwargs):
        if u"data-yt-key" not in self.html:
            new = u'%s%s%s%s%s' % (self.html[:13], 'data-yt-key="', settings.YT_API_KEY, '" ', self.html[13:])
            self.html = new
        super(YouTubeChannel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'YouTube канал'
        verbose_name_plural = u'YouTube каналы'

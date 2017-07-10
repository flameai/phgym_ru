# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .templatetags.mainapp_extras import register

from .models import *


def handler404(request):
    context = {}
    page = get_object_or_404(Page, slug='404')
    context.update({"page": page, "title": page.title})
    return render(request, 'mainapp/page.html', context)


def index(request, slug=None):
    context = {'indexpage': True}

    if slug:    # Главная страница клуба
        club = get_object_or_404(Club, slug=slug)

        try:
            sliders = Slider.objects.filter(club=club).order_by('order')
            context.update({'sliders': sliders})
        except:
            pass

        try:
            staticPage = StaticPage.objects.get(club=club)
            context.update({'staticpage': staticPage})
        except:
            pass

        try:
            fitneszone = FitnesZone.objects.filter(club=club)
            context.update({'fitneszones': fitneszone})
        except:
            pass

        try:
            channel = YouTubeChannel.objects.get(club=club)
            context.update({'channel': channel})
        except:
            try:
                channel = YouTubeChannel.objects.get(club__isnull=True)
                context.update({'channel': channel})
            except:
                pass

        return render(request, 'mainapp/index.html', context)
    else:   # Корпоративная страница
        try:
            sliders = Slider.objects.filter(club__isnull=True).order_by('order')
            context.update({'sliders': sliders})
        except:
            pass
        try:
            news = News.objects.all().order_by('-date')[:3]
            context.update({'news_list': news})
        except:
            pass
        try:
            staticpage = StaticPage.objects.get(club__isnull=True)
            context.update({'staticpage': staticpage})
        except:
            pass
        return render(request, 'mainapp/indexcompany.html', context)


def news(request, page=""):
    context = {}
    if page:  # вывод подробной статьи
        news = get_object_or_404(News, slug=page)
        breadcrumbs = [{"title": "Новости", "url": "/news/"},
                       {"title": news.title, "url": request.path, "active": True}]
        context.update({'breadcrumbs': breadcrumbs, 'news': news})
        return render(request, 'mainapp/news/item.html', context)
    else:  # вывод списка кратких статей
        news = News.objects.filter(hidden=False).order_by("-date")
        breadcrumbs = [{"title": "Новости", "url": request.path, "active": True}]
        context.update({'breadcrumbs': breadcrumbs, 'news_list': news})
        return render(request, 'mainapp/news/list.html', context)


def stock(request, slug="", page=""):
    context = {}
    club = get_object_or_404(Club, slug=slug)
    if page:  # вывод подробной статьи
        stock = get_object_or_404(Stock, slug=page, club=club)
        breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                       {'title': "Новости и акции", "url": "/" + slug + "/stock/"},
                       {'title': stock.title, "url": request.path, "active": True}]
        context.update({'breadcrumbs': breadcrumbs, 'stock': stock})
        return render(request, 'mainapp/stock/item.html', context)
    else:  # Вывод списка акций
        stocks = get_list_or_404(Stock, club=club, hidden=False)
        breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                       {'title': "Новости и акции", "url": request.path, "active": True}]
        context.update({'breadcrumbs': breadcrumbs, "stocks": stocks})
        return render(request, 'mainapp/stock/list.html', context)


def program(request, slug="", page=""):
    context = {}
    club = get_object_or_404(Club, slug=slug)
    if page:  # подробная статья
        prog = get_object_or_404(Program, club=club, slug=page)
        breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                       {'title': "Услуги", "url": '/' + slug + "/program/"},
                       {'title': prog.title, 'url': request.path, "active": True}]
        context.update({'breadcrumbs': breadcrumbs, "program": prog})
        return render(request, 'mainapp/program/item.html', context)
    else:  # список статей
        progs = get_list_or_404(Program, club=club)
        breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                       {'title': "Услуги", "url": request.path, "active": True}]
        context.update({"breadcrumbs": breadcrumbs, "programs": progs})
        try:
            editfield = EditTextField.objects.get(club=club, page=1)  # 1 - const program
            context.update({'editfield': editfield})
        except:
            pass
        return render(request, 'mainapp/program/list.html', context)


def schedule(request, slug="comsomoll", detail=None):
    schedule_num = detail
    club = get_object_or_404(Club, slug=slug)
    gym = get_object_or_404(Gym, club=club, pk=schedule_num)

    context = {}
    shedule = getDataByDays(gym)
    context.update({"shedule": shedule})
    
    breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                   {'title': u"Расписание %s" % gym.title, "url": request.path, "active": True}]
    context.update({'breadcrumbs': breadcrumbs})

    return render(request, 'mainapp/schedule.html', context)


def getDataByDays(gym):
    weekdays = WeekDay.objects.filter(gym=gym).order_by('day')
    output = []
    for weekday in weekdays:
        entries = Entry.objects.filter(weekday=weekday).order_by('time')
        day = {"day": weekday.get_day_display(), "data": entries}
        output.append(day)
    return output


def comments(request, slug="comsomoll"):
    context = {'title': u"Видеоблоги и отзывы"}
    return render(request, 'mainapp/comments.html', context)


def contacts(request, slug="comsomoll"):
    context = {}
    club = get_object_or_404(Club, slug=slug)
    breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                   {"title": "Контакты", "url": request.path, "active": True}]
    context.update({'breadcrumbs': breadcrumbs, 'club': club})
    return render(request, 'mainapp/contacts.html', context)


def call(request, slug=None):
    if request.POST:
        subject = request.POST.get('subject')
        name = request.POST.get('Name')
        tel = request.POST.get('Tel')

        msg = u"Телефон: " + tel + u" \r\nИмя: " + name

        FormRequest(formname=2, content=msg).save()
        emails = get_object_or_404(Club, slug=slug).emails_send.split(',')
        email = [x.strip() for x in emails]
        send_mail(subject, msg, settings.EMAIL_HOST_USER, email, fail_silently=True)

    context = {}
    if slug:
        club = get_object_or_404(Club, slug=slug)
        form = get_object_or_404(Form, club=club, form=2)
        breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                       {"title": form.title, "url": request.path, "active": True}]
        context.update({"breadcrumbs": breadcrumbs, "form": form})
    else:
        form = get_list_or_404(Form, form=2)[0]
        breadcrumbs = [{"title": form.title, "url": request.path, "active": True}]
        context.update({"breadcrumbs": breadcrumbs, "form": form})
    return render(request, 'mainapp/call.html', context)


def entry(request, slug="comsomoll"):

    if request.POST:
        subject = request.POST.get('subject')
        name = request.POST.get('Name')
        tel = request.POST.get('Tel')
        email = request.POST.get('Email')
        club = request.POST.get('Club')

        interview = request.POST.get('Interview')

        origin = request.POST.getlist('origin[]')
        service = request.POST.getlist('service[]')
        target = request.POST.getlist('target[]')
        parametr = request.POST.get('parametr')

        msg = u"Телефон: " + tel + u" \r\nИмя: " + name + u" \r\nE-mail: " + email
        if interview == "on":
            if origin:
                msg += u" \r\nИсточник:"
                for item in origin:
                    msg += u" " + item
            if service:
                msg += u" \r\nВажные услуги:"
                for item in service:
                    msg += u" " + item
            if target:
                msg += u" \r\nФитнес-цели:"
                for item in target:
                    msg += u" " + item
            if parametr:
                msg += u" \r\nОпределяющий параметр: " + parametr

        FormRequest(formname=1, content=msg).save()
        emails = get_object_or_404(Club, slug=slug).emails_send.split(',')
        email = [x.strip() for x in emails]
        send_mail(subject, msg, settings.EMAIL_HOST_USER, email, fail_silently=True)

    title = u"Заявка на бесплатный фитнес-день"
    context = {"title": title}
    club = get_object_or_404(Club, slug=slug)
    form = get_list_or_404(Form, club=club, form=1)[0]
    context.update({"form": form})
    return render(request, 'mainapp/form_entry.html', context)


def abonement(request, slug="comsomoll"):
    if request.POST:
        subject = request.POST.get('subject')
        name = request.POST.get('Name')
        tel = request.POST.get('Tel')

        msg = u"Телефон: " + tel + u" \r\nИмя: " + name

        FormRequest(formname=3, content=msg).save()

        emails = get_object_or_404(Club, slug=slug).emails_send.split(',')
        email = [x.strip() for x in emails]
        send_mail(subject, msg, settings.EMAIL_HOST_USER, email, fail_silently=True)

    club = get_object_or_404(Club, slug=slug)
    form = get_object_or_404(Form, club=club, form=3)
    breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                   {"title": form.title, "url": request.path, "active": True}]
    title = u"Заказать абонемент"
    context = {"title": title, "form": form}
    context.update({"breadcrumbs": breadcrumbs, "form": form})
    return render(request, 'mainapp/form_abonement.html', context)


def page(request, slug):
    context = {}
    page = get_object_or_404(Page, slug=slug)
    breadcrumbs = [{'title': page.title, 'url': request.path, "active": True }]
    context.update({"page": page, "breadcrumbs": breadcrumbs, "title": page.title})
    return render(request, 'mainapp/page.html', context)


@register.simple_tag
def getGymsForClubSlug(clubslug):
    gyms = []
    try:
        club = Club.objects.get(slug=clubslug)
        gyms_obj = Gym.objects.filter(club=club)
        for gym in gyms_obj:
            gyms.append({"name": gym.title, "id": gym.id})
    except:
        pass
    return gyms


@register.simple_tag
def getPhoneForClub(clubslug):
    try:
        club = Club.objects.get(slug=clubslug)
        phone = club.phone
        return phone
    except:
        pass


@register.simple_tag
def getClubInfo(slug):
    try:
        club = Club.objects.get(slug=slug)
        return club
    except:
        info = MainInfo.objects.first()
        return info


@register.simple_tag
def getMainPhone():
    try:
        info = MainInfo.objects.first()
        return info.phone
    except:
        pass


@register.simple_tag
def getClubs():
    try:
        clubs = Club.objects.all()
        return clubs
    except:
        pass


def weekDayByNum(num):
    day_of_week = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }
    return day_of_week[num]


def timeByNum(num):
    time = {
        1: "08:00 - 09:00",
        2: "09:00 - 10:00",
        3: "10:00 - 11:00",
        4: "11:00 - 12:00",
        5: "12:00 - 13:00",
        6: "13:00 - 14:00",
        7: "14:00 - 15:00",
        8: "15:00 - 16:00",
        9: "16:00 - 17:00",
        10: "17:00 - 18:00",
        11: "18:00 - 19:00",
        12: "19:00 - 20:00",
        13: "20:00 - 21:00",
        14: "21:00 - 22:00",
        15: "22:00 - 23:00",
    }
    return time[num]

# def getContext(page):
#     context = {}
#     try:
#         data = StaticPage.objects.get(pagetype=page)
#         context.update({"page": data })
#     except:
#         pass
#     return context

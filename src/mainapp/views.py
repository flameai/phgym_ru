# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .templatetags.mainapp_extras import register

from .models import *

def index(request, slug=""):
    context = {'indexpage': True}

    if slug:    # Главная страница клуба
        try:
            club = Club.objects.get(slug=slug)
        except:
            return  # обработать ошибку некорректного slug

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

        return render(request,'mainapp/index.html',context)
    else:   # Корпоративная страница
        try:
            sliders = Slider.objects.filter(club__isnull=True).order_by('order')
            context.update({'sliders': sliders})
        except:
            pass
        try:
            news = News.objects.all().order_by('-id')[:3]
            context.update({'news_list': news})
        except:
            pass
        try:
            staticpage = StaticPage.objects.get(club__isnull=True)
            context.update({'staticpage': staticpage})
        except:
            pass
        return render(request,'mainapp/indexcompany.html',context)


def news(request, page=""):
    context = {}
    if page:    # вывод подробной статьи
        try:
            news = News.objects.get(slug=page)
            breadcrumbs = [{"title": "Новости", "url": "/news/"}, {"title": news.title, "url": request.path, "active": True }]
            print(request)
            context.update({'breadcrumbs': breadcrumbs, 'news': news})
            return render(request,'mainapp/news/item.html', context)
        except:
            pass
    else:   # вывод списка кратких статей
        try:
            news = News.objects.all().order_by("-date")
            breadcrumbs = [{"title": "Новости", "url": request.path, "active": True }]
            context.update({'breadcrumbs': breadcrumbs, 'news_list': news})
            return render(request,'mainapp/news/list.html', context)
        except:
            pass


def stock(request, slug="", page=""):
    context = {}
    if page:    # вывод подробной статьи
        try:
            club = Club.objects.get(slug=slug)
            stock = Stock.objects.get(slug=page, club=club)
            breadcrumbs = [{'title': club.address, "url": "/"+slug+"/"},{'title': "Акции", "url": "/"+ slug + "/stock/"}, {'title': stock.title, "url": request.path, "active": True }]
            context.update({'breadcrumbs': breadcrumbs, 'stock': stock})
            return render(request,'mainapp/stock/item.html', context)
        except:
            pass
    else:   # Вывод списка акций
        try:
            club = Club.objects.get(slug=slug)
            stocks = Stock.objects.filter(club=club)
            breadcrumbs = [{'title': club.address, "url": "/"+slug+"/"},{'title': "Акции", "url": request.path, "active": True }]
            context.update({'breadcrumbs': breadcrumbs, "stocks": stocks })
            return render(request,'mainapp/stock/list.html',context)
        except:
            pass


def program(request, slug="", page=""):
    context = {}
    if page:    # подробная статья
        try:
            club = Club.objects.get(slug=slug)
            prog = Program.objects.get(club=club, slug=page)
            breadcrumbs = [{'title': club.address, "url": "/"+slug+"/"},{'title': "Программы", "url": '/'+slug+"/program/"},{'title': prog.title, 'url': request.path, "active": True}]
            context.update({'breadcrumbs': breadcrumbs, "program": prog})
            return render(request,'mainapp/program/item.html', context)
        except:
            pass
    else:       # список статей
        try:
            club = Club.objects.get(slug=slug)
            progs = Program.objects.filter(club=club)
            breadcrumbs = [{'title': club.address, "url": "/"+slug+"/"},{'title': "Программы", "url": request.path, "active": True }]
            context.update({"breadcrumbs": breadcrumbs, "programs": progs })
        except:
            pass
            
        try:
            editfield = EditTextField.objects.get(club=club, page=1) # 1 - const program
            context.update({'editfield': editfield})
        except:
            pass

        return render(request,'mainapp/program/list.html',context)


def schedule(request, slug="comsomoll", detail=None):
    schedule_num = detail
    club_num = getClubByName(slug)
    context = {}
    try:
        mobile = getDataByDays(club_num,schedule_num)
        desktop = getDataByTime(club_num,schedule_num)
        context.update({"desktop": desktop, "mobile": mobile})
        title = u"Расписание"
        subtitle = u"Расписание"
        context.update({'title': title, 'subtitle': subtitle})
        try:
            club = Club.objects.get(slug=slug)
            gym = Gym.objects.filter(club=club,pk=schedule_num)
            breadcrumbs = [{'title': club.address, "url": "/" + slug + "/"},
                           {'title': u"Расписание %s" % gym.title, "url": request.path, "active": True}]
            context.update({'breadcrumbs': breadcrumbs})
        except:
            pass
        print('work it')
    except:
        print('not work')
        pass
    return render(request,'mainapp/schedule.html', context)


def comments(request, slug="comsomoll"):
    context = {}
    try:
        title = u"Видеоблоги и отзывы"
        context.update({'title': title})
    except:
        pass
    return render(request,'mainapp/comments.html',context)


def contacts(request, slug="comsomoll"):
    context = {}
    try:
        club = Club.objects.get(slug=slug)
        breadcrumbs = [{'title': club.address, "url": "/"+slug+"/"},{"title": "Контакты", "url": request.path, "active": True}]
        context.update({'breadcrumbs': breadcrumbs, 'club': club})
    except:
        pass
    return render(request,'mainapp/contacts.html', context)


def call(request, slug=""):
    if request.POST:
        subject = request.POST.get('subject')
        name = request.POST.get('Name')
        tel = request.POST.get('Tel')

        msg = u"Телефон: " + tel + u" \r\nИмя: " + name

        FormRequest(formname=2, content=msg).save()

        if slug == "furmanova":
            send_mail(subject, msg, settings.EMAIL_HOST_USER, ['xservking@gmail.com','skif1976@gmail.com'], fail_silently=False)
        elif slug == "comsomoll":
            send_mail(subject, msg, settings.EMAIL_HOST_USER, ['smog_king@mail.ru','skif1976@gmail.com'], fail_silently=False)

    context = {}
    try:
        club = Club.objects.get(slug=slug)
        form = Form.objects.get(club=club,form=2)
        breadcrumbs = [{'title': club.address, "url": "/"+slug+"/"},{"title": form.title, "url": request.path, "active": True}]
        context.update({"breadcrumbs": breadcrumbs, "form": form })
    except:
        pass
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

        if club == u"Фурманова, 117":
            send_mail(subject, msg, settings.EMAIL_HOST_USER, ['xservking@gmail.com','skif1976@gmail.com'], fail_silently=False)
        elif club == u"ТРК КомсоМОЛЛ":
            send_mail(subject, msg, settings.EMAIL_HOST_USER, ['smog_king@mail.ru','skif1976@gmail.com'], fail_silently=False)


    title = u"Заявка на бесплатный фитнес-день"
    context = {"title": title}
    try:
        club = Club.objects.get(slug=slug)
        form = Form.objects.get(club=club,form=1)
        context.update({"form": form })
    except:
        pass

    return render(request, 'mainapp/form_entry.html', context)


def abonement(request, slug="comsomoll"):
    if request.POST:
        subject = request.POST.get('subject')
        name = request.POST.get('Name')
        tel = request.POST.get('Tel')

        msg = u"Телефон: " + tel + u" \r\nИмя: " + name

        FormRequest(formname=3, content=msg).save()

        if slug == "furmanova":
            send_mail(subject, msg, settings.EMAIL_HOST_USER, ['xservking@gmail.com','skif1976@gmail.com'], fail_silently=False)
        elif slug == "comsomoll":
            send_mail(subject, msg, settings.EMAIL_HOST_USER, ['smog_king@mail.ru','skif1976@gmail.com'], fail_silently=False)

    try:
        club = Club.objects.get(slug=slug)
        form = Form.objects.get(club=club,form=3)
        breadcrumbs = [{'title': club.address, "url": "/"+slug+"/"},{"title": form.title, "url": request.path, "active": True}]
        context.update({"breadcrumbs": breadcrumbs, "form": form })
    except:
        pass

    title = u"Заказать абонемент"
    context = {"title": title, "form": form}

    return render(request, 'mainapp/form_abonement.html', context)


def page(request, slug):
    context = {}
    try:
        page = Page.objects.get(slug=slug)
        breadcrumbs = [{'title': page.title, 'url': request.path, "active": True }]
        context.update({"page": page, "breadcrumbs": breadcrumbs})
    except:
        pass
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
        pass

@register.simple_tag
def getClubs():
    try:
        clubs = Club.objects.all()
        return clubs
    except:
        pass

def getDataByDays(clubnum,gymnum):
     club = Club.objects.get(pk=clubnum)
     gym = Gym.objects.filter(club=club,pk=gymnum)
     weekdays = WeekDay.objects.filter(gym=gym)
     entries = []
     for weekday in weekdays:
         entry = []
         for time in range(1,14):
             obj = Entry.objects.filter(weekday=weekday,time=time)
             if obj.exists():
                 obj = obj.get()
                 entry.append({"content": obj.content, "program": programByNum(obj.program), "time": timeByNum(obj.time)})
             else:
                 entry.append({"content": "", "program": "", "time": timeByNum(time)})
         obj = {"day": weekDayByNum(weekday.day), "data": entry}
         entries.append(obj)
     return entries

def getDataByTime(clubnum,gymnum):
    club = Club.objects.get(pk=clubnum)
    gym = Gym.objects.filter(club=club,pk=gymnum)
    weekdays = WeekDay.objects.filter(gym=gym)
    entries = []
    for time in range(1,14):
        entry = []
        for weekday in weekdays:
            obj = Entry.objects.filter(weekday=weekday,time=time)
            if obj.exists():
                obj = obj.get()
                entry.append({"content": obj.content, "program": obj.program})
            else:
                entry.append({"content": "", "program": ""})
        obj = {"time": timeByNum(time), "data": entry}
        entries.append(obj)
    return entries


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

def programByNum(num):
    program = {
        1: "topfitness",
        2: "studio",
        3: "other"
    }
    return program[num]

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

def getClubByName(name):
    club = Club.objects.get(slug=name)
    return club.pk

# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import SuitDateWidget, AutosizedTextarea
from suit.admin import SortableModelAdmin

from .models import *


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'date': SuitDateWidget,
            'title': AutosizedTextarea,
            'text': AutosizedTextarea,
        }

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_display_links = ('title', 'date')
    list_filter = ['date']
    form = NewsForm

admin.site.register(News, NewsAdmin)

admin.site.register(StaticPage)

class WeekDayInline(admin.TabularInline):
    model = WeekDay
    max_num = 7
    show_change_link = True

class GymInline(admin.TabularInline):
    model = Gym
    show_change_link = True

class EntryInline(admin.TabularInline):
    model = Entry
    max_num = 12


class ClubAdmin(admin.ModelAdmin):
    list_display = ('address','phone','email','worktime')
    inlines = [
        GymInline,
    ]

admin.site.register(Club,ClubAdmin)

class GymAdmin(admin.ModelAdmin):
    list_display = ('title','club')
    inlines = [
        WeekDayInline
    ]

admin.site.register(Gym,GymAdmin)

class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('day','gym')
    inlines = [
        EntryInline,
    ]

admin.site.register(WeekDay, WeekDayAdmin)

class SliderAdmin(SortableModelAdmin):
    list_display = ('title', 'club', 'order')
    sortable = 'order'

admin.site.register(Slider, SliderAdmin)

admin.site.register(Form)

class FormRequestAdmin(admin.ModelAdmin):
    list_display = ('formname', 'daterequest')

admin.site.register(FormRequest, FormRequestAdmin)

class PageAdmin(SortableModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'url')
    readonly_fields = ('url',)
    sortable = 'order'

admin.site.register(Page, PageAdmin)

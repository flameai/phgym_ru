# -*- coding: utf-8 -*-
from django.contrib import admin
from djangoseo.admin import register_seo_admin, get_inline
from seo import MyMetadata
from django.forms import ModelForm
from suit.widgets import SuitDateWidget, AutosizedTextarea, SuitSplitDateTimeWidget
from suit.admin import SortableModelAdmin
from .models import *

register_seo_admin(admin.site, MyMetadata)


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'date': SuitSplitDateTimeWidget,
            'title': AutosizedTextarea,
            'text': AutosizedTextarea,
        }


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date', 'shown')
    list_display_links = ('title', 'date')
    list_filter = ['date', ]
    form = NewsForm

    def shown(self, obj):
        return not(obj.hidden)
    shown.short_description = "показывается"
    shown.boolean = True


admin.site.register(News, NewsAdmin)


class WeekDayInline(admin.TabularInline):
    model = WeekDay
    max_num = 7
    show_change_link = True


class GymInline(admin.TabularInline):
    model = Gym
    show_change_link = True


class EntryInline(admin.TabularInline):
    model = Entry
    show_change_link = True
    fields = ('content', 'weekday', 'time', 'duration')


class ClubAdmin(SortableModelAdmin):
    list_display = ('address', 'phone', 'email', 'worktime', 'order')
    inlines = [GymInline, ]
    sortable = 'order'


admin.site.register(Club, ClubAdmin)


class GymAdmin(admin.ModelAdmin):
    list_display = ('title', 'club')
    inlines = [WeekDayInline, ]


admin.site.register(Gym, GymAdmin)


class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('day', 'gym')
    inlines = [EntryInline, ]


admin.site.register(WeekDay, WeekDayAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('content', 'time', 'duration', 'weekday', 'get_gym', 'get_club')

    def get_gym(self, obj):
        return obj.weekday.gym
    get_gym.short_description = u'зал'
    get_gym.admin_order_field = 'weekday__gym'

    def get_club(self, obj):
        return obj.weekday.gym.club
    get_club.short_description = u'клуб'
    get_club.admin_order_field = 'weekday__gym__club'


admin.site.register(Entry, EntryAdmin)


admin.site.register(EntryTemplate)


class SliderAdmin(SortableModelAdmin):
    list_display = ('title_internal', 'club', 'order')
    sortable = 'order'
    exclude = ('order',)


admin.site.register(Slider, SliderAdmin)


class FormAdmin(admin.ModelAdmin):
    readonly_fields = ('link',)


admin.site.register(Form, FormAdmin)


class FormRequestAdmin(admin.ModelAdmin):
    list_display = ('formname', 'daterequest')


admin.site.register(FormRequest, FormRequestAdmin)


class PageAdmin(SortableModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'url')
    readonly_fields = ('url',)
    sortable = 'order'


admin.site.register(Page, PageAdmin)


class StockAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date', 'club', 'shown')
    list_filter = ('date', 'club')

    def shown(self, obj):
        return not(obj.hidden)
    shown.short_description = "показывается"
    shown.boolean = True


admin.site.register(Stock, StockAdmin)


class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date', 'club')


admin.site.register(Program, ProgramAdmin)


class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'club',)


admin.site.register(StaticPage, StaticPageAdmin)


class FitnesZoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'club',)


admin.site.register(FitnesZone, FitnesZoneAdmin)


class EditTextFieldAdmin(admin.ModelAdmin):
    list_display = ('club', 'page',)


admin.site.register(EditTextField, EditTextFieldAdmin)
admin.site.register(YouTubeChannel)
admin.site.register(MainInfo)

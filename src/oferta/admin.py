from django.contrib import admin

from .models import Oferta

class OfertaAdmin(admin.ModelAdmin):
    readonly_fields = ('url',)


admin.site.register(Oferta, OfertaAdmin,)

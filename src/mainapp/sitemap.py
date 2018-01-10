# -*- coding: utf-8 -*-
from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.urls import reverse
from mainapp.models import News, Club, Stock, Program

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['index','news','/pages/franshiza/']

    def location(self, item):
        try:
            return reverse(item)
        except:
            return item
        

news = {
    'queryset': News.objects.filter(hidden=False)
}

clubs = {
    'queryset': Club.objects.filter()
}

stocks = {
    'queryset': Stock.objects.filter(hidden=False)
}

programs = {
    'queryset': Program.objects.filter()
}

sitemaps = {}
sitemaps['static'] = StaticViewSitemap()
sitemaps['news'] = GenericSitemap(news, priority=1, changefreq="daily")
sitemaps['news'].location = lambda x: "/news/" + x.slug + "/"
sitemaps['clubs'] = GenericSitemap(clubs, priority=0.5, changefreq="daily")
sitemaps['clubs'].location = lambda x: "/" + x.slug + "/"
sitemaps['contacts'] = GenericSitemap(clubs, priority=0.5, changefreq="weekly")
sitemaps['contacts'].location = lambda x: "/" + x.slug + "/contacts/"
sitemaps['program'] = GenericSitemap(clubs, priority=0.5, changefreq="daily")
sitemaps['program'].location = lambda x: "/" + x.slug + "/program/"
sitemaps['stock'] = GenericSitemap(clubs, priority=0.5, changefreq="daily")
sitemaps['stock'].location = lambda x: "/" + x.slug + "/stock/"
sitemaps['stocks'] = GenericSitemap(stocks, priority=1, changefreq="daily")
sitemaps['stocks'].location = lambda x: "/" + x.club.slug + "/stock/" + x.slug + "/"
sitemaps['programs'] = GenericSitemap(programs, priority=0.7, changefreq="daily")
sitemaps['programs'].location = lambda x: "/" + x.club.slug + "/program/" + x.slug + "/"
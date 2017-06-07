from django import template

register = template.Library()


@register.filter
def callable(value):
    return value.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')

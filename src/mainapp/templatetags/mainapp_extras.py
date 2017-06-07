from django import template

register = template.Library()

def callable(value):
    return value.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')

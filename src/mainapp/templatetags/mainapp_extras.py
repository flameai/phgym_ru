from django import template

register = template.Library()

def callable(phone):
    return phone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
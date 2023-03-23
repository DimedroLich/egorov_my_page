from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key= " "):
    return value.split(key)[0]

@register.filter(name='times')
def times(n):
    return range(n)

@register.filter(name='filter_range')
def filter_range(start,end):
    return range(start,end)
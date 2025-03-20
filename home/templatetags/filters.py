from  django import template
import datetime

register = template.Library()

# filter tags
@register.filter
def cutchars(value, arg):
    return value[:arg]


# create tag / simple tag
@register.simple_tag
def current_time(format_str):
    return datetime.datetime.now().strftime(format_str)

# create tag / inclusion tag
@register.inclusion_tag("home/result_tag.html")
def show_res(queryset):
    return {"objects" : queryset}
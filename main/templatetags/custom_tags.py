from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr_name):
    return getattr(obj, attr_name, None)

@register.simple_tag
def range_custom(start, end):
    return range(start, end)

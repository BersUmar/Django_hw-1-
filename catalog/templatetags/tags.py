from django import template

register = template.Library()

# Создание тега
@register.simple_tag
def mediapath(value):
    if value:
        return f"/media/{value}"
    else:
        return ''
from django import template

register = template.Library()


@register.filter(name='converter_date')
def converter_date(value):
    days = 15
    month = 12
    years = 2020
    hours = 0
    minutes = 0
    return f'{days:02d}:{month:02d}:{years:02d} в {hours:02d}:{minutes:02d}'
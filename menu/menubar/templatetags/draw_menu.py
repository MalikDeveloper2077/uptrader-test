from django import template
from django.shortcuts import get_object_or_404

from menubar.models import Menu


register = template.Library()


@register.inclusion_tag('menubar/menu.html', takes_context=True)
def draw_menu(context, menu_name: str) -> dict:
    menu_items = get_object_or_404(Menu, name=menu_name).items.filter(parent__isnull=True)
    return {'menu_items': menu_items, 'request': context['request']}


@register.filter('remove_url_slash')
def remove_url_slash(url: str) -> str:
    if url.startswith('/'):
        url = url[1:]
    if url.endswith('/'):
        url = url[:-1]
    return url

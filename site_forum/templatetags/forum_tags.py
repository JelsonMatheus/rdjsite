from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='rangepage')
def rangepage(page_obj, limit=4):
    num_pages = page_obj.paginator.num_pages

    start = max(page_obj.number - limit + 1, 1) if (page_obj.number < num_pages) \
        else max(num_pages - limit + 1, 1)

    end = min(page_obj.number, num_pages) if (page_obj.number >= limit) \
        else min(limit, num_pages)

    return [i for i in range(start, end + 1)]


@register.filter(name='shownotify')
def shownotify(notifi):
    html = f'''
        <button class="dropdown-item pe-3" data-notify="true" data-link="{notifi.data['url']}">
            <b>{notifi.actor.username}</b> respondeu em <span class="text-primary">{notifi.target}</span>
        </button>'''
    
    return mark_safe(html)


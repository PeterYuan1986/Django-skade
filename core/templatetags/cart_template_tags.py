from django import template
from core.models import Order, Category, Item
from django.template.loader import get_template

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            sm = 0
            for item in qs[0].items.all():
                sm += item.quantity
            return sm
    return 0

from django import template
from products.models import Testimonials, Products, Order, OrderProduct
from django.contrib.auth.models import User
register = template.Library()
from django.contrib import messages


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].products.count()
        else:
            return 0


# Get the items in the order of the signed in user
@register.filter
def get_users_order(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            context = {
                "order_list" :  qs
            }
            return  context
        return messages.error("You have no order ")


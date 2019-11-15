from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max, Avg, Min, Count, FloatField
from django.conf import settings
from django.views import generic
from django.contrib import messages
from django.http import Http404, JsonResponse, HttpResponseRedirect
from .forms import ProductCreateForm, SearchProductForm
from .models import Products, Order, OrderProduct, Testimonials, BilllingAddress
from django.views.generic import ListView, DetailView, TemplateView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import datetime
from .forms import CheckoutForm
import random


def home_views(request):
    form = SearchProductForm()

    products = Products.objects.all()[:8]
    testimonials = Testimonials.objects.filter(display=True).order_by('id')[:3]

    context = {
        "products": products,
        "testimonials": testimonials,
        "form": form,
    }

    return render(request, 'products/home.html',  context, {'title': 'Welcome Home'})

# Products List View
class ProductsListView(ListView):
    model = Products
    template_name = "products/productsList.html"

def ProductsView(request):
    products = Products.objects.all()[:8]

    context = {
        "products": products
    }
    return render(request, 'products/productsList.html',  context, {'title': 'All Products'})


# Order SUmmary
class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(
                user=self.request.user, ordered=False)
            context = {
                'order': order
            }
            return render(self.request, 'products/order-summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
            # About us View


# About view
class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()

        context = {
            "form": form
        }
        return render(self.request, 'products/checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(
                user=self.request.user, ordered=False)
            
            if form.is_valid():
                user = self.request.user
                street_address = form.cleaned_data.get("street_address")
                appartment_address = form.cleaned_data.get("appartment_address")
                country = form.cleaned_data.get("country")
                zip = form.cleaned_data.get("zip")
                same_billing_address = form.cleaned_data.get("same_billing_address")
                save_info = form.cleaned_data.get("save_info")
                payment_option = form.cleaned_data.get("payment_option")

                billing_addres= BilllingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    appartment_address = appartment_address,
                    country = country,
                    zip = zip,
                    same_billing_address = same_billing_address,
                    save_info = save_info,
                    payment_option = payment_option
                )

                billing_addres.save()
                order.billing_addres = billing_addres
                order.save()
                messages.success(self.request, f"{user} Thanks for your checkout")
                
            return redirect('/chechout/')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")

        context = {
            'form': form
        }
        return render(self.request, 'products/checkout.html', context)


def about_view(request):
    return render(request, 'products/about.html', {'title': "About Us"})


#  Create View
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get('product_category')
            form.save()
            messages.success(f'{product_name} saved successffuly')
    else:
        form = ProductCreateForm
    context = {
        'form': form
    }
    return render(request, 'products/product-create.html', context)


# Products More Details Section
class ProductDetail(DetailView):
    model = Products


@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Products, slug=slug)
    orderproduct, created = OrderProduct.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            orderproduct.quantity += 1
            orderproduct.save()
            messages.info(request, "This item quantity was updated")
            return redirect('/order-summary/')
        else:
            messages.info(request, "Added to cart")
            order.products.add(orderproduct)
            return redirect('/order-summary/')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered=False,
            ordered_date=ordered_date
        )
        order.products.add(orderproduct)
        return redirect('/order-summary/')


@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Products, slug=slug)
    order_qs = Order.objects.filter(
        # products=product,
        user=request.user,
        ordered=False
    )
    
    if order_qs.exists():
        order = order_qs[0]

        # Chech if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            order.products.remove(order_product)
            messages.info(request, "Item Was removed from your cart")
            return redirect("/order-summary/")

        else:
            messages.info(request, "This was removed")
            return redirect('/order-summary/')
    else:
        messages.info(request, "You do not have an order ")
        return redirect('/order-summary/',)


@login_required
def remove_single_item_from_cart(request, slug):
    product = get_object_or_404(Products, slug=slug)
    order_qs = Order.objects.filter(
        # products=product,
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]

        # Chech if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.products.remove(order_product)

            order_product.save()
            # order.products.remove(order_product)
            messages.info(request, "This item quantity was updated")
            return redirect("/order-summary")

        else:
            messages.info(request, "This was removed")
            return redirect('/order-summary/',)
    else:
        messages.info(request, "You do not have an order ")
        return redirect('/order-summary/',)


# Get Random '''Test'''
def get_random():
    max_id = Products.objects.all().aggregate(max_id=Max("id"))["max_id"]
    pk = random.randint(1, max_id)
    return Products.objects.get(pk=pk)
print(get_random)


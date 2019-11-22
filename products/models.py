from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.template.defaultfilters import slugify

from PIL import Image

select_op = [
    ('', "Select Product Type"),
]

TYPES_CHOICES = [
    ('MacBook Pro', 'MacBook Pro'),
    ('MacBook Air', 'MacBook Air'),
    ('iPad', 'iPad'),
    ('iMac', 'iMac'),
    ('iPhone', 'iPhone'),
]

IPHONE_CHOICES = [
    ('', "Select Iphone Type"),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
]

PRODUCT_STATE = (
    ('', "Select State"),
    ('New', 'New '),
    ('Used', 'Used '),
    ('Damaged', 'Damaged '),
)

YEAR_CHOICES = [
    ('', ' Select Year '),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
]

CONDITION_CHOICES = [
    ('', ' Select Condition '),
    ('Good', 'Good'),
    ('Perfect', 'Perfect'),
    ('Other', 'Other'),
]

cat_choices = select_op + TYPES_CHOICES


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_category = models.CharField(
        max_length=100, choices=cat_choices)
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES)
    product_state = models.CharField(max_length=20, choices=PRODUCT_STATE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    year = models.CharField(max_length=100, choices=YEAR_CHOICES, default="")
    inch = models.IntegerField(default="0")
    date_added = models.DateField(default=timezone.now, null=False)
    product_image = models.ImageField(
        default="products_image/default.png", upload_to="products_image")
    description = models.TextField(
        max_length=50000000, default="Say Something here")
    featured = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    display = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_category + "-" +
                            self.year + "-" + self.product_state)
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_category

    def get_absolute_url(self, *args, **kwargs):
        return reverse("product-detail", kwargs={
            "slug": self.slug
        })

    def add_to_cart_url(self, *args, **kwargs):
        return reverse("add-to-cart", kwargs={
            "slug": self.slug
        })

    def get_saved(self, *args, **kwargs):
        return self.price - self.discount_price

    def get_removed_from_cart(self, *args, **kwargs):
        return reverse('remove-from-cart', kwargs={
            "slug": self.slug
        })


class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.quantity } of { self.product.product_category }"

    def get_total_price(self):
        return self.quantity * self.product.price

    def get_discount_price(self):
        return self.quantity * self.product.discount_price

    def get_saved(self):
        return self.get_total_price() - self.get_discount_price()

    def final_price(self):
        if self.product.discount_price:
            print()
            return self.get_discount_price()
        else:
            return self.get_total_price
        print(final_p)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateField()
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        'BilllingAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    # To be Updated
    def get_total(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_total_price()
        return total


PAYMENT_CHOICE = (
    ('C', "Card"),
    ('S', "Stripe")
)


class BilllingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    appartment_address = models.CharField(max_length=200)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=200)
    same_billing_address = models.BooleanField(default=True)
    save_info = models.BooleanField(default=False)
    payment_option = models.CharField(
        max_length=2,  default=False, choices=PAYMENT_CHOICE)

    def __str__(self):
        return self.user.username


USER_TYPE_CHOICES = [
    ('', "Select User Type"),
    ('Client', "Client"),
    ('Supplyer', "Supplyer"),
    ('Employee', "Employee"),
    ('Developer', "Developer"),
]


class Testimonials(models.Model):
    fullName = models.CharField(max_length=100)
    testimonial = models.TextField()
    user_image = models.ImageField(
        default="testimonials-img/default.png", upload_to="testimonials-img")
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)
    date_posted = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.fullName

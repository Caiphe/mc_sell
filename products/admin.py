from django.contrib import admin
from . models import Products, OrderProduct, Order, Testimonials, BilllingAddress
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["product_category", "price",
                    "discount_price", "condition", "inch", "year"]
    list_filter = ('product_category', 'price')
    ordering = ('-date_added',)
    search_fields = ['product_category']
    fieldsets=[
        ("Primary Fields" ,{
            "description" : "These Fields are required",
            "fields" : (("user", "product_category", "condition", "product_state"), 
            ("price", "discount_price", "year"),
            ("inch", "date_added", "product_image"),
            ("featured", "sale", ),
            )
        }),
        ("Description / Slug ",{
            "fields": (("description", "slug"))
        })
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class TestimonialsAdmin(admin.ModelAdmin):
    t_display = ["fullName", "user_type"]

@admin.register(BilllingAddress)
class BilllingAddressAdmin(admin.ModelAdmin):
    list_display = ["user", "country","zip", "payment_option"]
    list_filter = ('payment_option', )
    search_fields = ['payment_option']


# class ProductsAdmin(admin.ModelAdmin):
admin.site.register(Order)
admin.site.register(OrderProduct)
# admin.site.register(BilllingAddress)
admin.site.register(Testimonials, TestimonialsAdmin)


from django.contrib import admin
from .models import *


class GalleryInline(admin.StackedInline):
    model = Gallery
    # extra = 3
    # max_num = 3
    # can_delete = False


class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'featured_image']
    inlines = [GalleryInline]


class CartInline(admin.StackedInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartInline]


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'item', 'quantity', 'price', 'cart']


admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Gallery)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
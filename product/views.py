from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views.generic import DetailView, View, ListView, CreateView, UpdateView, DeleteView
from .models import Item, Cart, CartItem, Category
from .forms import AddToCartForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .forms import CreateProduct
from django.urls import reverse_lazy
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemDetailView(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = super().get_object()
        context['form'] = AddToCartForm(instance=objects)
        return context


class AddToCartView(LoginRequiredMixin, View):

    def get(self, request):
        qty = request.GET.get('qty', 1)
        item_id = request.GET.get('item_id')
        item = Item.objects.get(pk=item_id)
        cart_obj, created = Cart.objects.get_or_create(user=request.user, is_activate=True)
        item, created = CartItem.objects.get_or_create(item=item, cart=cart_obj, defaults={'quantity': qty})
        if not created:
            item.quantity = item.quantity + int(qty)
            item.save()

        messages.success(request, 'product added your cart')
        return redirect('index')


class Checkout(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.get(user=request.user, is_activate=True)
        items = CartItem.objects.filter(cart=cart)
        # total_price = items.aggregate(total=Sum('price'))
        print(cart)

        # print(session.id)
        context = {
            'cart': cart,
            'items': items,
            'paypal_client_id': settings.PAYPAL_CLIENT_ID,
            # 'stripe_session_id': session.id,
            'stripe_public_key': settings.STRIPE_PUBLISHABLE_KRY
            # 'total_price': total_price['total']
        }
        return render(request, 'product/checkout.html', context)


class Create_Product(LoginRequiredMixin, CreateView):
    model = Item
    form_class = CreateProduct
    template_name = 'dashboard/dashboard/create_product.html'
    success_url = reverse_lazy('product-list')


class Product_Edit(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = CreateProduct
    template_name = 'dashboard/dashboard/create_product.html'
    success_url = reverse_lazy('product-list')


class Product_Delete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('product-list')
    template_name = 'dashboard/dashboard/product_confirm_delete.html'


class Product_Detail(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'dashboard/dashboard/product_detail.html'
    context_object_name = 'product'


class Product_List(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'dashboard/dashboard/product_list.html'
    context_object_name = 'products'


class Category_List(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'dashboard/dashboard/category_list.html'
    context_object_name = 'categorys'
from django.shortcuts import render
from django.views.generic import View
from product.models import Item


class HomeView(View):
    def get(self, request):
        # new_product = Item.objects.new_items()
        # top_product = Item.objects.top_items()
        all_items = Item.objects.all().select_related('category') # QUERY optimization
        new_product = all_items.order_by('-pk')[:10]
        top_product = all_items.order_by('-sell_count')[:10]
        context = {
            'new_product': new_product,
            'top_product': top_product
        }
        return render(request, 'index.html',context)

    def post(self, request):
        book = request.POST.get('book')
        print(book)
        return render(request, 'index.html')




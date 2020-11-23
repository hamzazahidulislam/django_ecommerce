import decimal
from django.db.models import Sum
from django.db import models
from django.contrib.auth.models import User

# class Gallery(models.Model):
#     photo = models.ImageField(upload_to='/product_images')


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ItemManager(models.Manager):
    def new_items(self):
        return self.all().select_related('category').order_by('-pk')[:10]

    def top_items(self):
        return self.all().select_related('category').order_by('-sell_count')[:10]


class Item(models.Model):
    SIZE_CHOICE = (
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L')
    )
    COLOR_CHOICE =(
        ('red', 'RED'),
        ('white', 'WHITE'),
        ('black', 'BLACK')
    )
    name = models.CharField(max_length=150)
    new_price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    description = models.TextField()
    size = models.CharField(max_length=5, choices=SIZE_CHOICE)
    color = models.CharField(max_length=5, choices=COLOR_CHOICE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now=True)
    sell_count = models.IntegerField(default=0)
    featured_image = models.ImageField(upload_to='featured_image', blank=True, null=True)
    objects = ItemManager()

    @property
    def discount(self):
        d = self.old_price - self.new_price
        d_rate = (d * 100) / self.old_price
        return d_rate

    def __str__(self):
        return self.name


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='gallery')

    def __str__(self):
        return str(self.pk)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_activate = models.BooleanField(default=True)

    def total_price(self):
        cart_items = self.cart_item.all()
        price = cart_items.aggregate(total=Sum('price'))
        print(price)
        return price['total']

    def __str__(self):
        return str(self.pk)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')

    def save(self,*args,**kwargs):
        self.price = self.item.new_price * decimal.Decimal(self.quantity)
        super().save(*args, **kwargs)
    # @property
    # def price(self):
    #     return self.quantity * self.item.new_price

    def __str__(self):
        return self.item.name
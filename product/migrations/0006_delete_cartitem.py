# Generated by Django 3.1 on 2020-08-26 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_cart_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]

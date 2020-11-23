# Generated by Django 3.1 on 2020-08-17 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('in_stock', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('size', models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L')], max_length=5)),
                ('color', models.CharField(choices=[('red', 'RED'), ('white', 'WHITE'), ('black', 'BLACK')], max_length=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]

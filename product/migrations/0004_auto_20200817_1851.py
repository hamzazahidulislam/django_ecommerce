# Generated by Django 3.1 on 2020-08-17 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='is_featured',
        ),
        migrations.AddField(
            model_name='item',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='featured_image'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='product.item'),
        ),
    ]

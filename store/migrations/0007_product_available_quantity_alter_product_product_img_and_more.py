# Generated by Django 4.0.1 on 2022-03-05 10:16

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_product_shop_img_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.PositiveIntegerField(default=0, help_text='Available Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, upload_to=store.models.get_unique_filepath),
        ),
        migrations.AlterField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='shop_img',
            field=models.ImageField(blank=True, upload_to=store.models.get_unique_filepath),
        ),
    ]
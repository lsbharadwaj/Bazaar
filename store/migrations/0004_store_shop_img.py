# Generated by Django 4.0.1 on 2022-02-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='shop_img',
            field=models.ImageField(blank=True, upload_to='shopImages/'),
        ),
    ]

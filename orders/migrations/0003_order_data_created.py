# Generated by Django 5.0.1 on 2024-02-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_goods_order_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='data_created',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
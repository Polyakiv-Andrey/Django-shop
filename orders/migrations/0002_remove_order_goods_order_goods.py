# Generated by Django 5.0.1 on 2024-02-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_remove_basket_goods_basket_goods'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='goods',
        ),
        migrations.AddField(
            model_name='order',
            name='goods',
            field=models.ManyToManyField(blank=True, related_name='order', to='basket.goods'),
        ),
    ]
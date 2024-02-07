# Generated by Django 5.0.1 on 2024-02-04 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basket', '0002_remove_basket_goods_basket_goods'),
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_status', models.CharField(choices=[('created', 'Created'), ('in_progress', 'In Progress'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='created', max_length=20)),
                ('user_id', models.CharField()),
                ('delivery_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='logistic.deliverydetail')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='basket.goods')),
            ],
        ),
    ]
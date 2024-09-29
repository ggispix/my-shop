# Generated by Django 5.1.1 on 2024-09-28 23:00

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cartitem_cart_alter_cartitem_quantity'),
        ('orders', '0013_alter_orderinfo_ordered_date_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 28, 23, 0, 26, 332771, tzinfo=datetime.timezone.utc)),
        ),
    ]

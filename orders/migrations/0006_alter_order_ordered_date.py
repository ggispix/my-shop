# Generated by Django 5.1.1 on 2024-09-26 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 17, 9, 22, 994885, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-26 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 20, 47, 42, 110205, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-18 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0007_auto_20200418_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_details',
            name='purchase_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

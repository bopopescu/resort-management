# Generated by Django 3.0.5 on 2020-04-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0009_auto_20200418_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_details',
            name='purchase_date',
            field=models.DateTimeField(verbose_name='purchase_date'),
        ),
    ]
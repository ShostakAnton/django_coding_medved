# Generated by Django 3.0.3 on 2020-02-19 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200219_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='prince_per_item',
            new_name='price_per_item',
        ),
    ]

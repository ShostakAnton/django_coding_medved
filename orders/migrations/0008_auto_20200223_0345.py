# Generated by Django 3.0.3 on 2020-02-23 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_productinbasket_session_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='nmd',
            new_name='nmb',
        ),
        migrations.RenameField(
            model_name='productinorder',
            old_name='nmd',
            new_name='nmb',
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20200213_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscibers',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='subscibers',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

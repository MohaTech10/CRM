# Generated by Django 3.1 on 2020-08-11 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_order_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='myApp.Tags'),
        ),
    ]

# Generated by Django 3.1 on 2020-08-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200811_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(auto_created=True, unique=True),
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-22 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_category_properties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='img',
        ),
    ]

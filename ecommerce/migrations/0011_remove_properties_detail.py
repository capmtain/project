# Generated by Django 4.2.4 on 2023-10-15 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_properties_image1_properties_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='detail',
        ),
    ]
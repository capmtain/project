# Generated by Django 4.2.4 on 2023-10-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_bikes_detail_cars_detail_mobile_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='image1',
            field=models.ImageField(null=True, upload_to='imgs'),
        ),
        migrations.AddField(
            model_name='properties',
            name='image2',
            field=models.ImageField(null=True, upload_to='imgs'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_remove_properties_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='detail',
            field=models.TextField(null=True),
        ),
    ]
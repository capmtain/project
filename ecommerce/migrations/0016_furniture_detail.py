# Generated by Django 4.2.4 on 2023-10-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_electronics_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='detail',
            field=models.TextField(null=True),
        ),
    ]

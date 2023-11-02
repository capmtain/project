# Generated by Django 4.2.4 on 2023-09-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('des', models.CharField(max_length=1000, null=True)),
                ('char', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
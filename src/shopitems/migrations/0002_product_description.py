# Generated by Django 3.2.9 on 2021-11-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopitems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Description'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-21 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopitems', '0002_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='books',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_tag',
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=0.5),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Добавь описание', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='shopitems.Product'),
        ),
    ]
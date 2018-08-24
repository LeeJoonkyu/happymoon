# Generated by Django 2.0.7 on 2018-08-22 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20180822_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_for_pad',
            name='product_del',
        ),
        migrations.AlterField(
            model_name='cart_for_pad',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
    ]
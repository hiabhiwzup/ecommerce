# Generated by Django 4.0.1 on 2022-02-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_orders_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=111),
        ),
    ]
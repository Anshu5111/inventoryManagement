# Generated by Django 5.0.4 on 2024-05-02 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
    ]

# Generated by Django 3.2 on 2023-04-23 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]
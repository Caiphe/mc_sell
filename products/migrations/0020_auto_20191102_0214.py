# Generated by Django 2.2.4 on 2019-11-02 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20191102_0207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='products',
        ),
    ]

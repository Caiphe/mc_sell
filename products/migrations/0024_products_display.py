# Generated by Django 2.2.4 on 2019-11-04 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20191102_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='condition',
            field=models.CharField(choices=[('', '-- Select Condition --'), ('Good', 'Good'), ('Perfect', 'Perfect'), ('Other', 'Other')], max_length=100),
        ),
    ]

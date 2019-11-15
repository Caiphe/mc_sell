# Generated by Django 2.2.4 on 2019-11-12 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0026_auto_20191112_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='BilllingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=200)),
                ('appartment_address', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=200)),
                ('same_billing_address', models.BooleanField(default=True)),
                ('save_info', models.BooleanField(default=False)),
                ('payment_option', models.CharField(choices=[('C', 'Card'), ('S', 'Stripe')], default=False, max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

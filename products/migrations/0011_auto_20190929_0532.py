# Generated by Django 2.2.4 on 2019-09-29 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190928_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='condition',
            field=models.CharField(choices=[('', ' Select Condition '), ('Good', 'Good'), ('Perfect', 'Perfect'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_category',
            field=models.CharField(choices=[('', ' Select Product Type '), ('MacBook Pro', 'MacBook Pro'), ('MacBook Air', 'MacBook Air'), ('iPad', 'iPad'), ('iPhone', 'iPhone')], max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='year',
            field=models.CharField(choices=[('', ' Select Year '), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019')], default='', max_length=100),
        ),
    ]
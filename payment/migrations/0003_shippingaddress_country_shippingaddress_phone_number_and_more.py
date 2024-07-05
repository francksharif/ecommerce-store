# Generated by Django 5.0.6 on 2024-07-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_shippingaddress_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(default='Canada', max_length=250),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zip_code',
            field=models.CharField(max_length=250),
        ),
    ]

# Generated by Django 4.0.3 on 2022-10-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_booking_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
# Generated by Django 4.1.2 on 2022-12-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_booking_options_alter_contactmail_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

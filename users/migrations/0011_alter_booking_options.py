# Generated by Django 4.1.2 on 2022-11-14 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_booking_options_booking_is_cancelled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['is_confirmed', '-created']},
        ),
    ]

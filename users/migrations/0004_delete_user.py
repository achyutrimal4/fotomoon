# Generated by Django 4.1.2 on 2022-11-03 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
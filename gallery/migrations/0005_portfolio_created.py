# Generated by Django 4.1.2 on 2022-11-03 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_portfolio_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
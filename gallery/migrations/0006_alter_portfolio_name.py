# Generated by Django 4.1.2 on 2022-11-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_portfolio_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Portfolio Name'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-03 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_portfolio_photoportfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/portfolio/', verbose_name='Cover Photo'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_alter_packages_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='available',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=200, verbose_name='Is available?'),
        ),
    ]
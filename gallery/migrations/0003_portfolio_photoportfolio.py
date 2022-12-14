# Generated by Django 4.1.2 on 2022-11-03 02:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_photo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('name', models.CharField(max_length=255, verbose_name='Portfolio')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoPortfolio',
            fields=[
                ('description', models.CharField(max_length=250, null=True)),
                ('photo', models.ImageField(upload_to='images/portfolio/')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.portfolio', verbose_name='Portfolio')),
            ],
        ),
    ]

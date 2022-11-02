# Generated by Django 4.1.2 on 2022-11-02 11:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='images/news/')),
                ('imageBy', models.CharField(default='Fotomoon Admin', max_length=200)),
                ('author', models.CharField(blank=True, default='Fotomoon Admin', max_length=200, null=True)),
                ('photo_caption', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-04 02:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMail',
            fields=[
                ('full_name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=200, null=True)),
                ('phone_number', models.IntegerField()),
                ('subject', models.CharField(max_length=200, null=True)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
    ]

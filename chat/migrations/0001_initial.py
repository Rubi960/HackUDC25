# Generated by Django 5.1.6 on 2025-02-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100000)),
                ('response', models.CharField(max_length=100000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

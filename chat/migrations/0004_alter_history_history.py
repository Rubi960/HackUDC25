# Generated by Django 5.1.6 on 2025-02-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_alter_history_history"),
    ]

    operations = [
        migrations.AlterField(
            model_name="history",
            name="history",
            field=models.JSONField(default=list),
        ),
    ]

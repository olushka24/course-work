# Generated by Django 4.2.10 on 2024-02-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0005_completedcourse"),
    ]

    operations = [
        migrations.AddField(
            model_name="completedcourse",
            name="mark",
            field=models.IntegerField(default="0"),
            preserve_default=False,
        ),
    ]

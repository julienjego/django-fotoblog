# Generated by Django 4.1.5 on 2023-01-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="word_count",
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 4.1.10 on 2023-11-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DisneylandReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Review_ID", models.IntegerField()),
                ("Rating", models.IntegerField()),
                ("Year", models.IntegerField()),
                ("Text", models.CharField(max_length=255)),
                ("Branch", models.CharField(max_length=255)),
            ],
        ),
    ]
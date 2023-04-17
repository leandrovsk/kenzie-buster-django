# Generated by Django 4.2 on 2023-04-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0004_alter_movie_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(default=None, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_trailers_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

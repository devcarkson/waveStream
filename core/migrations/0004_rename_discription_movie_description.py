# Generated by Django 5.0.6 on 2024-06-09 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_movie_trailer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='discription',
            new_name='description',
        ),
    ]

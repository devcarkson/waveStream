# Generated by Django 5.0.6 on 2024-06-29 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_movie_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tag1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
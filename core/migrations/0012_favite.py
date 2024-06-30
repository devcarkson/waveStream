# Generated by Django 5.0.6 on 2024-06-30 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=32)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.movie')),
            ],
            options={
                'unique_together': {('session_id', 'movie')},
            },
        ),
    ]

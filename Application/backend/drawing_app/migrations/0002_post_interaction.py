# Generated by Django 3.1.5 on 2021-04-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='interaction',
            field=models.IntegerField(default=0),
        ),
    ]

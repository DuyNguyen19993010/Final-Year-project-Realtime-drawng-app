# Generated by Django 3.1.5 on 2021-04-06 02:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drawing_app', '0005_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_update_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 2, 0, 48, 174177, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 2, 0, 48, 174177, tzinfo=utc)),
        ),
    ]

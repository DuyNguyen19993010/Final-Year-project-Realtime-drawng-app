# Generated by Django 3.1.1 on 2020-11-11 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drawing_app', '0002_room_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canvas_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='drawing_app.request')),
            ],
            bases=('drawing_app.request',),
        ),
        migrations.AddField(
            model_name='request',
            name='requester',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drawing_app.profile'),
        ),
        migrations.AddField(
            model_name='request',
            name='room',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drawing_app.room'),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drawing_app.room')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drawing_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
                ('canvas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drawing_app.canvas')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='canvas',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='drawing_app.canvas'),
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together={('requester', 'room')},
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='drawing_app.request')),
                ('invited', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drawing_app.profile')),
            ],
            bases=('drawing_app.request',),
        ),
    ]

# Generated by Django 2.2.13 on 2021-03-18 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210318_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]

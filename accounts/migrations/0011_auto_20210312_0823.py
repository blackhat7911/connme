# Generated by Django 3.0.7 on 2021-03-12 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_relationship_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 3.0.7 on 2021-03-10 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210310_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 2.1.2 on 2018-11-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20181120_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timelinetask',
            name='client_note',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wedding',
            name='location',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]

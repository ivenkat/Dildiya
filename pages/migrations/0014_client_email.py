# Generated by Django 2.1.2 on 2018-12-17 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20181215_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

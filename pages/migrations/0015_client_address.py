# Generated by Django 2.1.2 on 2018-12-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

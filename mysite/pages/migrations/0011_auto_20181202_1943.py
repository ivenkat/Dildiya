# Generated by Django 2.1.2 on 2018-12-03 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20181202_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bride_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='groom_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
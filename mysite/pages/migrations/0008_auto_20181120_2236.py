# Generated by Django 2.1.2 on 2018-11-21 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20181120_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetlineitem',
            name='contracted_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='budgetlineitem',
            name='estimated_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='budgetlineitem',
            name='payment_price',
            field=models.IntegerField(),
        ),
    ]

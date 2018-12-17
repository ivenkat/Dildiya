# Generated by Django 2.1.2 on 2018-12-02 23:41

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20181120_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.AlterField(
            model_name='client',
            name='bride_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='groom_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='wedding',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Wedding'),
        ),
    ]
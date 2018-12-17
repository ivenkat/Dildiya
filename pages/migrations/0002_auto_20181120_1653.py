# Generated by Django 2.1.2 on 2018-11-20 21:53

from django.db import migrations, models
import django.db.models.deletion
import pages.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('vendor_type', models.CharField(choices=[(pages.models.VendorTypes('Photographer'), 'Photographer'), (pages.models.VendorTypes('Videographer'), 'Videographer'), (pages.models.VendorTypes('Decorator'), 'Decorator'), (pages.models.VendorTypes('Caterer'), 'Caterer'), (pages.models.VendorTypes('Bartender'), 'Bartender')], max_length=5)),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('contact_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('vendor_location', models.CharField(max_length=200)),
                ('booked', models.BooleanField(default=False)),
                ('website', models.CharField(max_length=200)),
                ('events', models.ManyToManyField(to='pages.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='vendor',
            name='weddings',
            field=models.ManyToManyField(to='pages.Wedding'),
        ),
        migrations.AddField(
            model_name='event',
            name='wedding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Wedding'),
        ),
        migrations.AddField(
            model_name='client',
            name='wedding',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.Wedding'),
        ),
    ]

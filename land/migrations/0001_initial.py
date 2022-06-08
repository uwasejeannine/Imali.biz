# Generated by Django 4.0.4 on 2022-05-25 08:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=240, null=True)),
                ('last_name', models.CharField(max_length=240, null=True)),
                ('email_addres', models.EmailField(default='your email address', max_length=240, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='Phone number', max_length=128, region=None)),
                ('land_size', models.CharField(default='hectare', max_length=240, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.CharField(max_length=255)),
                ('zooning', models.CharField(max_length=240, null=True)),
                ('cost_sqm', models.CharField(max_length=240, null=True)),
                ('upi_number', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]

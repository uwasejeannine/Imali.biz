# Generated by Django 4.0.4 on 2022-07-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='signature',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

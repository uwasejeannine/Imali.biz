# Generated by Django 4.0.4 on 2022-07-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machmaking', '0007_remove_mach_hello'),
    ]

    operations = [
        migrations.AddField(
            model_name='mach',
            name='cost_sqm',
            field=models.BigIntegerField(null=True),
        ),
    ]

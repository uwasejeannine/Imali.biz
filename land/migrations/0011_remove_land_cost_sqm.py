# Generated by Django 4.0.4 on 2022-07-14 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0010_land_cost_sqm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='land',
            name='cost_sqm',
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-27 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machmaking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mach',
            name='benefit',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='contraction',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='engineer',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='land_size',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='rio',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='sale_price_rwf',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='status',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='total_cost_rwf',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='unit_type',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='upi',
        ),
        migrations.RemoveField(
            model_name='mach',
            name='zonning',
        ),
    ]

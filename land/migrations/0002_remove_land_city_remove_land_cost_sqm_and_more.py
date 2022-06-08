# Generated by Django 4.0.4 on 2022-05-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='land',
            name='city',
        ),
        migrations.RemoveField(
            model_name='land',
            name='cost_sqm',
        ),
        migrations.RemoveField(
            model_name='land',
            name='email_addres',
        ),
        migrations.RemoveField(
            model_name='land',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='land',
            name='land_size',
        ),
        migrations.RemoveField(
            model_name='land',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='land',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='land',
            name='upi_number',
        ),
        migrations.RemoveField(
            model_name='land',
            name='zooning',
        ),
        migrations.AddField(
            model_name='land',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='land',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='land',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='land',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='land',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='land',
            name='price',
            field=models.FloatField(),
        ),
    ]

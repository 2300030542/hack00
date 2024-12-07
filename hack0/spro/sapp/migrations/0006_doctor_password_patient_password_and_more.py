# Generated by Django 4.1.7 on 2023-04-07 12:12

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0005_remove_appointments_afternoontoken_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default=123456, max_length=100000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookedappointments',
            name='appointment_preference',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bookedappointments',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bookedappointments',
            name='slot',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='hospitalid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='pincode',
            field=models.CharField(default=111111, max_length=6, validators=[django.core.validators.RegexValidator(message='Enter a valid Indian pincode.', regex='^[0-9]{6}$')]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pincode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter a valid Indian pincode.', regex='[0-9]{6}$')]),
        ),
    ]

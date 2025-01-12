# Generated by Django 5.1.1 on 2024-09-26 15:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='ABN',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='email',
            field=models.EmailField(max_length=255, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='service',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_name',
            field=models.CharField(choices=[('PL', 'Plumbing'), ('EL', 'Electrical'), ('CL', 'Cleaning'), ('CT', 'Construction')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_provider',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

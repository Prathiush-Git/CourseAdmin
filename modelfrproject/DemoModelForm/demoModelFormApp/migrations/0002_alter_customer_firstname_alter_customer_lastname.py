# Generated by Django 4.0.1 on 2022-03-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoModelFormApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='firstname',
            field=models.CharField(default='firstname', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastname',
            field=models.CharField(blank=True, max_length=20, verbose_name='Surname'),
        ),
    ]
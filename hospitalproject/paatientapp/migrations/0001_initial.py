# Generated by Django 4.2.4 on 2023-08-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patientb',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('disease', models.CharField(max_length=30)),
                ('pa_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='festtb',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('fest_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]

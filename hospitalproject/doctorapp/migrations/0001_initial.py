# Generated by Django 4.2.4 on 2023-08-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctortb',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('dr_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
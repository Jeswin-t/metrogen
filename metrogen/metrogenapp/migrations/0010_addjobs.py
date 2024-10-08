# Generated by Django 4.2.2 on 2023-06-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrogenapp', '0009_fair'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddJobs',
            fields=[
                ('jobid', models.IntegerField(primary_key=True, serialize=False)),
                ('ref', models.CharField(max_length=20)),
                ('vaccancy', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('quali', models.CharField(max_length=20)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrogenapp', '0011_jobapply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='cus_id',
            field=models.CharField(max_length=20),
        ),
    ]

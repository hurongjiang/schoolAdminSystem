# Generated by Django 2.2.1 on 2019-08-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bytype',
            name='bytype',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='sex',
            name='sex',
            field=models.CharField(max_length=2),
        ),
    ]

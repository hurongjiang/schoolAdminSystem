# Generated by Django 2.2.1 on 2019-08-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolrool', '0003_auto_20190825_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolrool',
            name='entrance_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-27 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 27, 4, 49, 46, 890459, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 3.2.15 on 2022-09-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1990-04-24'),
            preserve_default=False,
        ),
    ]

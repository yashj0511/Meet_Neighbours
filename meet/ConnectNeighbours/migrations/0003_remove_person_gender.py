# Generated by Django 4.0.4 on 2023-08-05 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConnectNeighbours', '0002_person_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Gender',
        ),
    ]

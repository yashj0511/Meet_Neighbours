# Generated by Django 4.0.4 on 2023-08-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConnectNeighbours', '0003_remove_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True),
        ),
    ]

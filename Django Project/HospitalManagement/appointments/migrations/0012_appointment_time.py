# Generated by Django 3.2.8 on 2021-10-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_timeslot_eachslottime'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

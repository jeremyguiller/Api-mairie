# Generated by Django 3.1.7 on 2021-03-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapi', '0015_remove_location_confirmer'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='confirmer',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]

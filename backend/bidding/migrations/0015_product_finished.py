# Generated by Django 4.2 on 2023-04-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0014_placedbid_own'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]

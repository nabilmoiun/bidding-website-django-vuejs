# Generated by Django 4.2 on 2023-04-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='01631848044', max_length=13),
            preserve_default=False,
        ),
    ]
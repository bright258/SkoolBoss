# Generated by Django 4.0 on 2022-07-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_schoolprofile_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='wallet',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
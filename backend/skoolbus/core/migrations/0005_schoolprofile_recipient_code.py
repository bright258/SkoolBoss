# Generated by Django 4.0 on 2022-07-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_schoolprofile_name_of_school_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='recipient_code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

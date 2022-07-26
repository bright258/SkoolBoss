# Generated by Django 4.0 on 2022-07-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_document_alter_schoolprofile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='school_bio',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AddField(
            model_name='teacher',
            name='schools_map',
            field=models.FileField(blank=True, null=True, upload_to='then'),
        ),
    ]

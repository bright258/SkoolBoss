# Generated by Django 4.0 on 2022-07-20 09:26

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_rename_course_duration_schoolprofile_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='user',
            field=models.ForeignKey(default='Free', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school', to='core.user'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='documents',
            field=models.ManyToManyField(to='core.Document'),
        ),
    ]

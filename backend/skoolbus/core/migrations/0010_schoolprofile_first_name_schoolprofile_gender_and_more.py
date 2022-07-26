# Generated by Django 4.0 on 2022-07-19 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_upadated_at_course_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='firstname'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=200, null=True, verbose_name='gender'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='lastname'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='phonenumber'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='programme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.programme'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

# Generated by Django 4.0 on 2022-07-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_course_lecturer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

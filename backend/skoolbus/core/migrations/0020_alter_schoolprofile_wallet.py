# Generated by Django 4.0 on 2022-07-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_teacher_school_bio_teacher_schools_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='wallet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, null=True),
        ),
    ]

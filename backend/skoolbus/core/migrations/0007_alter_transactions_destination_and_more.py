# Generated by Django 4.0 on 2022-07-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_paystacak_reference_transactions_paystack_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='destination',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='paystack_reference',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

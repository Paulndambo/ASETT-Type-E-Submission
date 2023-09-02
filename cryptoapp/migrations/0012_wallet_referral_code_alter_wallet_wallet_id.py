# Generated by Django 4.2.4 on 2023-09-02 05:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0011_alter_portfolio_currency_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='referral_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('c35e121a-4682-436d-bfee-abb026350e07')),
        ),
    ]
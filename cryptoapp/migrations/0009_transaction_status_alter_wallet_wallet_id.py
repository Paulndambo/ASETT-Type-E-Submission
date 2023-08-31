# Generated by Django 4.2.4 on 2023-08-31 16:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0008_alter_wallet_wallet_id_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('6796d28f-c10d-4b24-8be0-f42e531656b1')),
        ),
    ]
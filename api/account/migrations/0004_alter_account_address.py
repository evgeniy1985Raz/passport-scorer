# Generated by Django 4.1.4 on 2022-12-14 08:44

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_community_rules"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="address",
            field=account.models.EthAddressField(max_length=100),
        ),
    ]

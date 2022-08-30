# Generated by Django 4.1 on 2022-08-30 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enderecos", "0001_initial"),
        ("core", "0004_pontoturistico_avaliacoes"),
    ]

    operations = [
        migrations.AddField(
            model_name="pontoturistico",
            name="endereco",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="enderecos.endereco",
            ),
        ),
    ]
# Generated by Django 4.1 on 2022-08-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_pontoturistico_endereco"),
    ]

    operations = [
        migrations.AddField(
            model_name="pontoturistico",
            name="foto",
            field=models.ImageField(
                blank=True, null=True, upload_to="pontos_turisticos"
            ),
        ),
    ]

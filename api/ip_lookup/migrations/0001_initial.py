# Generated by Django 4.1.3 on 2022-11-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IPv6Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip_from", models.BigIntegerField(unique=True)),
                ("ip_to", models.BigIntegerField(unique=True)),
                ("country_code", models.CharField(max_length=2)),
                ("country_name", models.CharField(max_length=64)),
                ("region_name", models.CharField(max_length=128)),
                ("city_name", models.CharField(max_length=128)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("zip_code", models.CharField(max_length=30)),
                ("time_zone", models.CharField(max_length=8)),
                ("version", models.CharField(default=6, max_length=1)),
            ],
            options={
                "abstract": False,
                "unique_together": {("ip_from", "ip_to")},
            },
        ),
        migrations.CreateModel(
            name="IPv4Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip_from", models.BigIntegerField(unique=True)),
                ("ip_to", models.BigIntegerField(unique=True)),
                ("country_code", models.CharField(max_length=2)),
                ("country_name", models.CharField(max_length=64)),
                ("region_name", models.CharField(max_length=128)),
                ("city_name", models.CharField(max_length=128)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("zip_code", models.CharField(max_length=30)),
                ("time_zone", models.CharField(max_length=8)),
                ("version", models.CharField(default=4, max_length=1)),
            ],
            options={
                "abstract": False,
                "unique_together": {("ip_from", "ip_to")},
            },
        ),
    ]
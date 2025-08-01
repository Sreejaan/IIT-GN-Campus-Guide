# Generated by Django 5.2 on 2025-06-01 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_mapstep"),
    ]

    operations = [
        migrations.CreateModel(
            name="WaterAndWashroom",
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
                ("name", models.CharField(max_length=100)),
                (
                    "facility_type",
                    models.CharField(
                        choices=[
                            ("washroom", "Washroom"),
                            ("water_point", "Water Point"),
                            ("both", "Both"),
                        ],
                        max_length=20,
                    ),
                ),
                ("google_maps_url", models.URLField()),
                ("location_note", models.TextField(blank=True)),
                ("building", models.CharField(blank=True, max_length=50)),
                ("floor", models.IntegerField(blank=True, null=True)),
                ("accessibility", models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name="person",
            name="phone_number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

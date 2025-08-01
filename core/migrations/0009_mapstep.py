# Generated by Django 5.2 on 2025-05-31 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_department_designation_person_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MapStep",
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
                ("step_number", models.PositiveIntegerField()),
                ("map_embed_url", models.URLField()),
                ("description", models.TextField(blank=True)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="map_steps",
                        to="core.person",
                    ),
                ),
            ],
            options={
                "ordering": ["step_number"],
            },
        ),
    ]

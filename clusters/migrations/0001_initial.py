# Generated by Django 4.2.16 on 2024-12-04 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cluster",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("endpoint", models.URLField(help_text="Airflow API endpoint URL")),
                (
                    "api_key",
                    models.CharField(
                        help_text="API key for authentication", max_length=255
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="ClusterHealth",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("healthy", "Healthy"),
                            ("unhealthy", "Unhealthy"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=20,
                    ),
                ),
                ("scheduler_status", models.CharField(max_length=20)),
                ("dag_processor_status", models.CharField(max_length=20)),
                ("metadata_db_status", models.CharField(max_length=20)),
                ("checked_at", models.DateTimeField(auto_now_add=True)),
                (
                    "cluster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="health_checks",
                        to="clusters.cluster",
                    ),
                ),
            ],
            options={
                "ordering": ["-checked_at"],
                "get_latest_by": "checked_at",
            },
        ),
    ]

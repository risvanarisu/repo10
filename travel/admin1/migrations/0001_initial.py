# Generated by Django 4.1.7 on 2023-08-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admins",
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
                ("name", models.TextField(db_column="admin_name", max_length=30)),
                ("contact", models.TextField(db_column="admin_contact", max_length=30)),
                ("email", models.TextField(db_column="admin_email", max_length=30)),
                (
                    "username",
                    models.TextField(db_column="admin_username", max_length=30),
                ),
                (
                    "password",
                    models.TextField(db_column="admin_password", max_length=30),
                ),
            ],
            options={
                "db_table": "admins",
            },
        ),
    ]

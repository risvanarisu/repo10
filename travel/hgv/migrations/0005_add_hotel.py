# Generated by Django 4.1.7 on 2023-06-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hgv", "0004_rename_image_add_guide_gui_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Add_hotel",
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
                ("hotel_name", models.TextField(db_column="-hotelame", max_length=50)),
                ("place", models.TextField(db_column="_place", max_length=50)),
                ("price", models.IntegerField(db_column="_price")),
                ("star", models.IntegerField(db_column="_star")),
                ("Address", models.TextField(db_column="_address", max_length=100)),
                ("contact", models.IntegerField(db_column="_contact")),
                ("email", models.TextField(db_column="_email", max_length=50)),
                ("features", models.TextField(db_column="_features", max_length=50)),
                (
                    "account_no",
                    models.TextField(db_column="_account no", max_length=50, null=True),
                ),
                (
                    "ifsc_code",
                    models.TextField(db_column="_ifsc code", max_length=50, null=True),
                ),
                (
                    "bank_name",
                    models.TextField(db_column="_bank name", max_length=50, null=True),
                ),
                (
                    "hotel_image",
                    models.ImageField(db_column="_hotelimage", upload_to="images/"),
                ),
            ],
            options={
                "db_table": "add_hotel",
            },
        ),
    ]
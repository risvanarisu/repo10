# Generated by Django 4.1.7 on 2023-06-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hgv", "0007_alter_add_vehicle_model_alter_add_vehicle_vehicle_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="add_vehicle",
            name="vehicle_id",
            field=models.IntegerField(db_column="_vehicleid"),
        ),
    ]
# Generated by Django 4.1.7 on 2023-06-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hgv", "0011_alter_add_guide_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="add_guide",
            name="contact",
            field=models.TextField(db_column="contact"),
        ),
        migrations.AlterField(
            model_name="add_hotel",
            name="contact",
            field=models.TextField(db_column="_contact"),
        ),
        migrations.AlterField(
            model_name="add_vehicle",
            name="contact",
            field=models.TextField(db_column="_contact"),
        ),
    ]

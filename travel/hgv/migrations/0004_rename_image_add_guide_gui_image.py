# Generated by Django 4.1.7 on 2023-06-07 14:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hgv", "0003_add_guide"),
    ]

    operations = [
        migrations.RenameField(
            model_name="add_guide",
            old_name="image",
            new_name="gui_image",
        ),
    ]
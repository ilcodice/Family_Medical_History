# Generated by Django 5.0 on 2024-12-15 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Medication", "0003_alter_medication_medicametion_costs_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="medication",
            old_name="medicametion_costs",
            new_name="medication_costs",
        ),
    ]

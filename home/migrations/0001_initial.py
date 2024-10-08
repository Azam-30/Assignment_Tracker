# Generated by Django 4.2.4 on 2024-08-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataStructuresStudent",
            fields=[
                (
                    "roll_no",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                (
                    "assignment1",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment2",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment3",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment4",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment5",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment6",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "roll_no",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                (
                    "assignment1",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment2",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment3",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment4",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment5",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
                (
                    "assignment6",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=3,
                    ),
                ),
            ],
            options={
                "verbose_name": "Python Student",
                "verbose_name_plural": "Python Students",
            },
        ),
    ]

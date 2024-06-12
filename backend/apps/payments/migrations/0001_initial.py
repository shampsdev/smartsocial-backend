# Generated by Django 5.0.6 on 2024-06-12 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("booking", "0004_delete_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                ("payment_id", models.CharField(blank=True, max_length=255, null=True)),
                ("return_url", models.TextField(blank=True, null=True)),
                (
                    "confirmation_token",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[
                            ("pending", "Ожидание оплаты"),
                            ("paid", "Оплачено"),
                            ("failed", "Ошибка оплаты"),
                            ("refunded", "Возврат средств"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="booking.cart"
                    ),
                ),
            ],
        ),
    ]

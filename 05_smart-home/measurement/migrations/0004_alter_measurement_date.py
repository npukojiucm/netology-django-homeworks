# Generated by Django 4.1 on 2022-09-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("measurement", "0003_alter_measurement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="date",
            field=models.DateField(auto_now_add=True, verbose_name="Date"),
        ),
    ]
